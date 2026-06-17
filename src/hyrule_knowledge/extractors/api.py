"""Static API and schema extraction helpers."""

from __future__ import annotations

import ast
import re
from dataclasses import dataclass, field

from hyrule_knowledge.github_source import read_file, run_text
from hyrule_knowledge.models import RepoSnapshot

HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}
GO_HANDLE_RE = re.compile(r"(?:HandleFunc|Handle)\(\s*[\"']([^\"']+)[\"']\s*,\s*([^,)]+)")


@dataclass(frozen=True)
class ApiEndpointInfo:
    method: str
    route: str
    source_path: str
    line: int
    end_line: int | None = None
    function_name: str | None = None
    docstring: str | None = None
    request_models: list[str] = field(default_factory=list)
    response_model: str | None = None
    return_annotation: str | None = None
    dependencies: list[str] = field(default_factory=list)
    status_codes: list[int] = field(default_factory=list)
    router_name: str | None = None
    handler_symbol: str | None = None


@dataclass(frozen=True)
class PydanticFieldInfo:
    name: str
    type: str
    default: str | None = None
    required: bool = True
    description: str | None = None


@dataclass(frozen=True)
class PydanticModelInfo:
    name: str
    source_path: str
    line: int
    end_line: int | None
    bases: list[str]
    docstring: str | None
    fields: list[PydanticFieldInfo]
    validators: list[str]


class _RouteVisitor(ast.NodeVisitor):
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.router_prefixes: dict[str, str] = {}
        self.endpoints: list[ApiEndpointInfo] = []

    def visit_Assign(self, node: ast.Assign) -> None:
        prefix = _apirouter_prefix(node.value)
        if prefix is not None:
            for target in node.targets:
                if isinstance(target, ast.Name):
                    self.router_prefixes[target.id] = prefix
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self._visit_function(node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self._visit_function(node)

    def _visit_function(self, node: ast.AsyncFunctionDef | ast.FunctionDef) -> None:
        for decorator in node.decorator_list:
            route = _route_from_decorator(decorator)
            if route is None:
                continue
            router_name, method, path, response_model, decorator_status = route
            prefix = self.router_prefixes.get(router_name or "", "")
            full_path = _join_route(prefix, path)
            request_models, dependencies = _function_inputs(node)
            status_codes = sorted({*decorator_status, *_http_exception_statuses(node)})
            self.endpoints.append(
                ApiEndpointInfo(
                    method=method.upper(),
                    route=full_path,
                    source_path=self.source_path,
                    line=node.lineno,
                    end_line=getattr(node, "end_lineno", None),
                    function_name=node.name,
                    docstring=ast.get_docstring(node),
                    request_models=request_models,
                    response_model=response_model,
                    return_annotation=ast.unparse(node.returns) if node.returns else None,
                    dependencies=dependencies,
                    status_codes=status_codes,
                    router_name=router_name,
                )
            )
        self.generic_visit(node)


class _ModelVisitor(ast.NodeVisitor):
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.models: list[PydanticModelInfo] = []

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        bases = [ast.unparse(base) for base in node.bases]
        if not _looks_like_pydantic_model(bases):
            self.generic_visit(node)
            return
        fields: list[PydanticFieldInfo] = []
        validators: list[str] = []
        for stmt in node.body:
            if isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name):
                fields.append(_field_from_annassign(stmt))
            elif isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if any(_decorator_name(d).endswith("validator") or "field_validator" in _decorator_name(d) for d in stmt.decorator_list):
                    validators.append(stmt.name)
        self.models.append(
            PydanticModelInfo(
                name=node.name,
                source_path=self.source_path,
                line=node.lineno,
                end_line=getattr(node, "end_lineno", None),
                bases=bases,
                docstring=ast.get_docstring(node),
                fields=fields,
                validators=validators,
            )
        )
        self.generic_visit(node)


def _decorator_name(node: ast.AST) -> str:
    if isinstance(node, ast.Call):
        return ast.unparse(node.func)
    return ast.unparse(node)


def _looks_like_pydantic_model(bases: list[str]) -> bool:
    return any(base.endswith("BaseModel") or base == "BaseModel" for base in bases)


def _field_from_annassign(node: ast.AnnAssign) -> PydanticFieldInfo:
    assert isinstance(node.target, ast.Name)
    default: str | None = None
    required = True
    description: str | None = None
    if node.value is not None:
        required = False
        default = _safe_default(node.value)
        description = _field_description(node.value)
    return PydanticFieldInfo(
        name=node.target.id,
        type=ast.unparse(node.annotation),
        default=default,
        required=required,
        description=description,
    )


def _safe_default(node: ast.AST) -> str:
    if isinstance(node, ast.Constant):
        if isinstance(node.value, str):
            return "<string>"
        return repr(node.value)
    text = ast.unparse(node)
    if len(text) > 80:
        return text[:77] + "..."
    return text


def _field_description(node: ast.AST) -> str | None:
    if not isinstance(node, ast.Call):
        return None
    for keyword in node.keywords:
        if keyword.arg == "description" and isinstance(keyword.value, ast.Constant):
            if isinstance(keyword.value.value, str):
                return keyword.value.value
    return None


def _apirouter_prefix(node: ast.AST) -> str | None:
    if not isinstance(node, ast.Call):
        return None
    func = ast.unparse(node.func)
    if not func.endswith("APIRouter"):
        return None
    for keyword in node.keywords:
        if keyword.arg == "prefix" and isinstance(keyword.value, ast.Constant):
            if isinstance(keyword.value.value, str):
                return keyword.value.value
    return ""


def _route_from_decorator(node: ast.AST) -> tuple[str | None, str, str, str | None, list[int]] | None:
    if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
        return None
    method = node.func.attr.lower()
    if method not in HTTP_METHODS:
        return None
    router_name = ast.unparse(node.func.value)
    if not node.args or not isinstance(node.args[0], ast.Constant) or not isinstance(node.args[0].value, str):
        return None
    path = node.args[0].value
    response_model: str | None = None
    status_codes: list[int] = []
    for keyword in node.keywords:
        if keyword.arg == "response_model":
            response_model = ast.unparse(keyword.value)
        elif keyword.arg == "status_code":
            value = _status_int(keyword.value)
            if value is not None:
                status_codes.append(value)
    return router_name, method, path, response_model, status_codes


def _status_int(node: ast.AST) -> int | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return node.value
    text = ast.unparse(node)
    match = re.search(r"(\d{3})", text)
    return int(match.group(1)) if match else None


def _join_route(prefix: str, path: str) -> str:
    if not prefix:
        return path or "/"
    return f"/{prefix.strip('/')}/{path.strip('/')}".replace("//", "/")


def _function_inputs(node: ast.AsyncFunctionDef | ast.FunctionDef) -> tuple[list[str], list[str]]:
    request_models: list[str] = []
    dependencies: list[str] = []
    defaults = list(node.args.defaults)
    args_with_defaults = node.args.args[len(node.args.args) - len(defaults) :]
    default_by_arg = {arg.arg: default for arg, default in zip(args_with_defaults, defaults, strict=False)}
    for arg in node.args.args + node.args.kwonlyargs:
        annotation = ast.unparse(arg.annotation) if arg.annotation is not None else ""
        if annotation and _looks_like_request_model(annotation):
            request_models.append(annotation)
        default = default_by_arg.get(arg.arg)
        if default is not None and isinstance(default, ast.Call) and ast.unparse(default.func).endswith("Depends"):
            dependencies.append(ast.unparse(default.args[0]) if default.args else arg.arg)
    for arg, default in zip(node.args.kwonlyargs, node.args.kw_defaults, strict=False):
        if default is not None and isinstance(default, ast.Call) and ast.unparse(default.func).endswith("Depends"):
            dependencies.append(ast.unparse(default.args[0]) if default.args else arg.arg)
    return sorted(dict.fromkeys(request_models)), sorted(dict.fromkeys(dependencies))


def _looks_like_request_model(annotation: str) -> bool:
    if annotation in {"Request", "Response", "BackgroundTasks"}:
        return False
    return annotation.endswith("Request") or annotation.endswith("Body") or annotation.endswith("Payload")


def _http_exception_statuses(node: ast.AST) -> list[int]:
    statuses: list[int] = []
    for child in ast.walk(node):
        if not isinstance(child, ast.Call):
            continue
        if not ast.unparse(child.func).endswith("HTTPException"):
            continue
        if child.args:
            value = _status_int(child.args[0])
            if value is not None:
                statuses.append(value)
        for keyword in child.keywords:
            if keyword.arg == "status_code":
                value = _status_int(keyword.value)
                if value is not None:
                    statuses.append(value)
    return statuses


def _python_files(snapshot: RepoSnapshot) -> list[str]:
    raw = run_text(["git", "ls-files", "*.py"], cwd=snapshot.path, allow_failure=True)
    return sorted(line.strip() for line in raw.splitlines() if line.strip())


def _go_files(snapshot: RepoSnapshot) -> list[str]:
    raw = run_text(["git", "ls-files", "*.go"], cwd=snapshot.path, allow_failure=True)
    return sorted(line.strip() for line in raw.splitlines() if line.strip())


def extract_python_api(snapshot: RepoSnapshot) -> tuple[list[ApiEndpointInfo], list[PydanticModelInfo]]:
    endpoints: list[ApiEndpointInfo] = []
    models: list[PydanticModelInfo] = []
    for rel_path in _python_files(snapshot):
        text = read_file(snapshot.path, rel_path)
        try:
            tree = ast.parse(text)
        except SyntaxError:
            continue
        route_visitor = _RouteVisitor(rel_path)
        route_visitor.visit(tree)
        endpoints.extend(route_visitor.endpoints)
        model_visitor = _ModelVisitor(rel_path)
        model_visitor.visit(tree)
        models.extend(model_visitor.models)
    return endpoints, models


def extract_go_api(snapshot: RepoSnapshot) -> list[ApiEndpointInfo]:
    endpoints: list[ApiEndpointInfo] = []
    for rel_path in _go_files(snapshot):
        text = read_file(snapshot.path, rel_path)
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in GO_HANDLE_RE.finditer(line):
                route = match.group(1)
                handler = match.group(2).strip()
                endpoints.append(
                    ApiEndpointInfo(
                        method="ANY",
                        route=route,
                        source_path=rel_path,
                        line=line_number,
                        function_name=handler,
                        handler_symbol=handler,
                    )
                )
    return endpoints


def extract_api(snapshot: RepoSnapshot) -> tuple[list[ApiEndpointInfo], list[PydanticModelInfo]]:
    endpoints, models = extract_python_api(snapshot)
    endpoints.extend(extract_go_api(snapshot))
    return endpoints, models


def model_concept_id(repo_slug: str, model_name: str) -> str:
    return f"generated/schemas/{repo_slug}/{model_name}"
