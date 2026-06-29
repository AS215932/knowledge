FROM python:3.12-slim AS runtime

ENV PYTHONUNBUFFERED=1 \
    UV_NO_CACHE=1 \
    PATH="/app/.venv/bin:${PATH}" \
    HYRULE_KNOWLEDGE_DB=/app/exports/knowledge.sqlite \
    HYRULE_KNOWLEDGE_MCP_TRANSPORT=streamable-http \
    HYRULE_KNOWLEDGE_MCP_BIND=0.0.0.0 \
    HYRULE_KNOWLEDGE_MCP_PORT=8767 \
    HYRULE_KNOWLEDGE_MCP_PATH=/mcp

RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates curl git \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:0.9.17 /uv /uvx /usr/local/bin/

WORKDIR /app

COPY pyproject.toml uv.lock README.md knowledge-policy.yml ./
COPY src ./src
COPY exports ./exports

RUN uv sync --frozen --no-dev --extra mcp

EXPOSE 8767

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import json, os, urllib.request; payload=json.loads(urllib.request.urlopen(f'http://127.0.0.1:{os.environ.get(\"HYRULE_KNOWLEDGE_MCP_PORT\", \"8767\")}/health', timeout=3).read()); raise SystemExit(0 if payload.get('status') == 'ok' else 1)"

CMD ["hyrule-knowledge-mcp"]
