# generated/source-docs/as215932/hyrule-mcp

* [Hyrule MCP](readme.md) - `hyrule-mcp` is the live diagnostic substrate for Hyrule Networks (AS215932). It exposes narrow, bounded Model Context Protocol tools for monitoring, routing, host, firewall, and packet-path inspection.
* [pyproject.toml](pyproject-toml.md) - [project] name = "hyrule-mcp" version = "0.1.0" description = "MCP server exposing AS215932 infrastructure tools (SSH, Prometheus, Icinga2, FRR, DNS)" requires-python = ">=3.14" dependencies = [ "mcp>=1.27.0", "paramiko>=4.0.0", "httpx>=...
* [Testing](testing.md) - Run the hermetic MCP characterization and regression suite with:
