# Alion MCP — jobs, companies and people for AI agents

<img src="assets/logo.png" alt="Alion" width="72" align="right">

Alion is a live graph of companies worldwide, built from the companies' own websites, job boards and public registers. It also holds the profiles of professionals open to offers who chose to be found by agents. This MCP server gives Claude, ChatGPT, Codex, Cursor and any MCP client access to it:

- **what a company is** — what it does, where it operates, its size, founding year and offices;
- **how it is funded** — funding rounds, amounts, dates, investors and accelerators;
- **what it builds with** — the technologies named in its own job postings;
- **how fast it grows** — hiring momentum, new offices and technologies, a dated story of its stages;
- **who is like it** — lookalike companies with the reasons they are similar;
- **the labour market** — verified job postings and pay, demand and time-to-fill statistics;
- **people** — professionals open to offers, searchable by role, skills, country and work mode, with a first message delivered through Alion (contacts are never served).

Use it for market maps, competitor and lookalike lists, sales prospecting, startup and deal-flow scouting, due diligence on a company, technology-adoption research and labour-market questions.

**Try without an account:** `https://alion.io/mcp/open` · **Full server:** `https://alion.io/mcp` (Streamable HTTP, OAuth 2.1) · **Docs:** https://alion.io/developers/agents · **Examples:** [examples/](examples/)

| Address | What it serves | Sign-in |
|---|---|---|
| `https://alion.io/mcp/open` | Compact searches of jobs and companies, full job postings, the people tools, watches | none (daily limit per network) |
| `https://alion.io/mcp` | Every tool | OAuth or API key |
| `https://alion.io/mcp/jobs` | Job search, postings, pay statistics, `my_matches` | OAuth or API key |
| `https://alion.io/mcp/companies` | Companies, lookalikes, the market | OAuth or API key |
| `https://alion.io/mcp/people` | Finding and messaging people | OAuth or API key |

> This repository holds the public manifests of the hosted server (MCP Registry `server.json` and `server-jobs.json`, `server-companies.json`, `server-people.json` for the narrow addresses, an Agent Plugins `plugin.json` + `mcp.json`), the connection guide and [examples](examples/). The server itself runs at alion.io; there is nothing to install or self-host.

## Tools

The company and job tools are read-only (`readOnlyHint: true`).

| Tool | What it answers |
|---|---|
| `search_companies` | Companies by industry, country, size, founding year, startup, funding stage, rounds raised since a date, minimum round, investor or accelerator, technology, growth level |
| `similar_companies` | Lookalikes of a company: shared industry segments and technologies, same headquarters country, a near size band |
| `get_company` | One company in depth: offices, funding rounds and investors, backers, stack, hiring and growth, traction, a dated story of its stages |
| `resolve_company` | The company behind a name, a domain or a URL, and whether it is alive |
| `search_jobs` | Live job postings verified on the employers' own boards, with pay (stated or estimated) |
| `get_job` | One posting in full: requirements, technologies, benefits, lifecycle |
| `market_stats` | Pay percentiles, demand and its trend, time to fill and top employers for a slice of the job market |
| `search_people`, `match_people`, `similar_people` | People open to offers for a role (by skills with years, seniority, country, the countries they may work in, work mode, languages, budget), for a vacancy, or like a given person |
| `get_person`, `check_fit` | One open profile; whether an offer passes the person's own filters before you write |
| `send_message`, `get_conversation`, `list_conversations` | A first message to a person, delivered into their Alion inbox, and the replies |
| `agent_status`, `verify_company`, `set_webhook` | The agent's limits and standing, proving the company it writes for, replies pushed to a webhook |
| `watch_search`, `check_watch`, `list_watches`, `delete_watch` | A saved search of jobs, companies or people that answers only what is new since the last check |
| `my_matches` | The job postings Alion matched to the signed-in person's profile |

The server also exposes 9 prompts (`company_research`, `market_map`, `startup_scout`, `market_brief`, `job_shortlist`, `hire_people`, `find_job_for_me`, `talent_map`, `prospect_list`) and 5 dictionary resources (`alion://dictionaries/...`: industries, countries, role families, ATS vendors, fixed vocabularies).

### Try

- "Find companies similar to mambu.com and explain what they have in common."
- "Which early-stage startups in Germany raised a round in the last year?"
- "Tell me about finmid.com: funding and investors, tech stack, and how fast it is growing."
- "Fintech companies in the UAE with 51-200 people that use Kubernetes."
- "What do backend engineers earn in Germany, and which companies hire the most of them?"
- "Find data engineers with Spark who can work in the Netherlands and show me the five best."
- "Watch remote Go backend roles for me and tell me what is new each morning."

Every answer links to the Alion page of each company or job posting.

## Connect

No account: use `https://alion.io/mcp/open` in place of `https://alion.io/mcp` below and skip the sign-in. With an account (free) the client opens the OAuth sign-in page on first use.

| Client | How |
|---|---|
| **Claude** (claude.ai, Desktop) | Settings → Connectors → Add custom connector → URL `https://alion.io/mcp` → Connect |
| **ChatGPT** | Settings → Apps & Connectors → Advanced → Developer mode → Create → URL `https://alion.io/mcp`, authentication OAuth |
| **Claude Code** | `claude mcp add --transport http alion https://alion.io/mcp`, then `/mcp` to sign in |
| **Cursor** | add to `~/.cursor/mcp.json`: `{"mcpServers": {"alion": {"url": "https://alion.io/mcp"}}}` |
| **VS Code** (Copilot) | Command palette → *MCP: Add Server* → HTTP → `https://alion.io/mcp` |
| **Cline** | MCP Servers → Configure → add `"alion": {"type": "streamableHttp", "url": "https://alion.io/mcp", "headers": {"Authorization": "Bearer <key>"}}` (step by step: [llms-install.md](llms-install.md)) |
| **Codex** | `codex mcp add alion --url https://alion.io/mcp`, then `codex mcp login alion` |
| **Mistral Le Chat** | add a custom MCP connector with URL `https://alion.io/mcp` and OAuth sign-in |
| **Any MCP client** | Streamable HTTP endpoint `https://alion.io/mcp`; OAuth discovery at `https://alion.io/.well-known/oauth-protected-resource/mcp` (dynamic client registration and client ID metadata documents are supported) |

Scripts can use an API key instead of OAuth: `Authorization: Bearer <key>` from https://alion.io/developers/keys. Every tool is also a plain HTTP endpoint (`/mcp/rest/<tool>`), described in OpenAPI 3.1 at https://alion.io/mcp/openapi; the live tool catalogue with input and output schemas is at https://alion.io/mcp/tools.

## Pricing

- On `https://alion.io/mcp/open`, compact lists (up to 20 rows), job postings, the people tools and watches are **free** within a daily limit per network.
- Compact lists (`detail="compact"`, up to 20 rows) of `search_companies`, `similar_companies` and `search_jobs` are **free up to 50 a day** for an assistant connected through OAuth.
- The people tools and watches are free on every address, within limits that grow with the agent's trust (no account, a signed-in wallet, an Alion account, a verified company).
- Full company profiles, job records and market statistics are paid from Alion credits (1 credit = $0.10; a company profile costs a few cents). Every result carries `meta` with what the call cost and what is left.
- `resolve_company` is free. Prices: https://alion.io/developers/pricing

## Data and privacy

Company and posting texts are third-party content: they are filtered for text aimed at AI models before they are served, and the tools present them as data, never as instructions. Contacts of people are not exposed. The server logs the tool name and its arguments (capped at 512 characters), the client name, status and duration for quotas, billing and abuse prevention, kept 12 months; it never reads conversation content, memory or history.

- Terms and privacy for the MCP server and API: https://alion.io/api-terms
- Privacy policy: https://alion.io/privacy · Terms of service: https://alion.io/terms

## Listings

- MCP Registry: `io.alion/alion`, `io.alion/jobs`, `io.alion/companies`, `io.alion/people`
- Smithery: https://smithery.ai/servers/alion/company-intelligence

## Support

https://alion.io/contact · dmitrii@alion-team.com

## License

The manifests and documentation in this repository are MIT licensed (see [LICENSE](LICENSE)). The Alion service and its data are covered by https://alion.io/api-terms.
