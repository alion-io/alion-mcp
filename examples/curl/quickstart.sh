#!/usr/bin/env bash
# The Alion MCP server over plain HTTP: JSON-RPC 2.0, one POST per call, no session.
# No account needed on the open address. Usage: bash quickstart.sh "Backend" DE
set -euo pipefail
URL="https://alion.io/mcp/open"
ROLE="${1:-Backend}"
COUNTRY="${2:-DE}"

rpc() {
  curl -s "$URL" \
    -H 'Content-Type: application/json' \
    -H 'Accept: application/json, text/event-stream' \
    -d "$1"
  echo
}

# 1. who is there
rpc '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"alion-curl-example","version":"1.0"}}}'

# 2. the tools (names only, if jq is installed)
if command -v jq >/dev/null; then
  rpc '{"jsonrpc":"2.0","id":2,"method":"tools/list"}' | jq -r '.result.tools[].name'
fi

# 3. the newest live postings for a role in a country
rpc '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"search_jobs","arguments":{"role":"'"$ROLE"'","country":"'"$COUNTRY"'","detail":"compact","limit":5}}}'
