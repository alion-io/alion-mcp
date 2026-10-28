"""A saved search with the MCP Python SDK: no model at all, just the tools.

    pip install mcp
    python daily_watch.py            # the first run saves the watch and prints what matches now
    python daily_watch.py            # every later run prints only what appeared since (cron it daily)

The watch belongs to the agent that made it: on the open address that is your network and client name,
with an account (Authorization: Bearer <key>) it is your account. The id is kept in .alion_watch.
"""
import asyncio
import json
import pathlib

from mcp import ClientSession, types
from mcp.client.streamable_http import streamablehttp_client

URL = "https://alion.io/mcp/open"
STATE = pathlib.Path(".alion_watch")
FILTERS = {"role": "Backend", "technology": "Go", "work_mode": "remote", "posted_since": "14d"}


def rows(result: types.CallToolResult) -> dict:
    return result.structuredContent or json.loads(result.content[0].text)


async def main() -> None:
    async with streamablehttp_client(URL) as (read, write, _):
        async with ClientSession(read, write, client_info=types.Implementation(name="alion-daily-watch", version="1.0")) as s:
            await s.initialize()
            if STATE.exists():
                res = rows(await s.call_tool("check_watch", {"watch_id": STATE.read_text().strip()}))
                items = res.get("new", [])
                print(f"{len(items)} new since {res.get('since')}")
            else:
                res = rows(await s.call_tool("watch_search", {"kind": "jobs", "filters": FILTERS, "name": "Remote Go backend"}))
                STATE.write_text(res["watch_id"])
                items = res.get("items", [])
                print(f"watching {res['watch_id']}: {len(items)} match now")
            for job in items:
                print(f"- {job['title']} · {job['company']['name']} · {job['url']}")


if __name__ == "__main__":
    asyncio.run(main())
