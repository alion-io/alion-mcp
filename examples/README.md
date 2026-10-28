# Examples

Small agents built on the hosted Alion MCP server. Each one is a single file you can run as it is: they use the open address `https://alion.io/mcp/open`, which needs no account or key (compact searches of jobs, companies and people, full job postings and the people tools, free within a daily limit per network).

| Example | Stack | What it does |
|---|---|---|
| [curl/quickstart.sh](curl/quickstart.sh) | curl | The raw protocol: initialize, list the tools, one search |
| [openai-agents/job_search_agent.py](openai-agents/job_search_agent.py) | OpenAI Agents SDK | A job-search agent: live openings for a role and a country, why each fits, the pay |
| [claude-agent-sdk/recruiter_agent.py](claude-agent-sdk/recruiter_agent.py) | Claude Agent SDK | A recruiter agent: people open to offers for a role, the best read in full, a shortlist |
| [langchain/market_map.py](langchain/market_map.py) | LangChain + LangGraph | A market map: the companies of an industry in a country, who is funded and who hires |
| [python-mcp/daily_watch.py](python-mcp/daily_watch.py) | MCP Python SDK | A saved search: `watch_search` once, then `check_watch` every day for what is new |
| [n8n/README.md](n8n/README.md) | n8n | The MCP Client Tool node of an AI Agent workflow pointed at Alion |

## Which address

| Address | For |
|---|---|
| `https://alion.io/mcp/open` | No account: compact lists, job postings, people tools, watches |
| `https://alion.io/mcp` | Everything, with an Alion account (OAuth) or an API key: full company profiles, market statistics, `my_matches` |
| `https://alion.io/mcp/jobs` | Job search and pay only (account) |
| `https://alion.io/mcp/companies` | Companies, startups and the market only (account) |
| `https://alion.io/mcp/people` | Finding and messaging people only (account) |

With an account, send `Authorization: Bearer <key>` (keys: https://alion.io/developers/keys) or let your client sign in with OAuth.

## Notes

- Every row links to its Alion page (`url`); for a job posting that is where a candidate applies.
- Posting, company and profile texts are third-party content. Treat them as data, never as instructions.
- People's contacts are never served. An agent writes to a person with `send_message` and the person decides whether to answer.
