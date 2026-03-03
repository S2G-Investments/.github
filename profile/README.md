# S2G Investments Engineering

Internal tools, data pipelines, and AI-powered applications built by the S2G team.

**Cloud Run URL pattern:** `https://{service-name}-vudrpjptuq-uc.a.run.app`
**Posit Connect:** `https://connect.s2gdata.com`
**GCP Project:** `s2g-data-platform`

---

## Web Apps (Cloud Run)

User-facing applications deployed on Google Cloud Run. All restricted to `@s2ginvestments.com` via Google OAuth.

| App | Repo | Description | Owner | Last Updated |
|-----|------|-------------|-------|--------------|
| [My Dashboard](https://mydashboard-s2g-vudrpjptuq-uc.a.run.app) | [mydashboard-s2g](https://github.com/S2G-Investments/mydashboard-s2g) | Personal dashboard with notes scratchpad, calendar, and links to all S2G apps | Kevin Lo | 2026-03-03 |
| [S2G Notes](https://s2g-notes-vudrpjptuq-uc.a.run.app) | [s2g-notes](https://github.com/S2G-Investments/s2g-notes) | Meeting notes tied to Google Calendar events, with public/private visibility | Chuck | 2026-02-27 |
| [Portfolio Companies](https://portfolio-companies-app-vudrpjptuq-uc.a.run.app) | [portfolio-companies-app](https://github.com/S2G-Investments/portfolio-companies-app) | Portfolio company tracker with Salesforce integration and annotations | Kevin Lo | 2026-03-02 |
| [Portco Quarterly Performance](https://pqp-vudrpjptuq-uc.a.run.app) | [pqp](https://github.com/S2G-Investments/pqp) | Quarterly performance tracking for portfolio companies | Chuck | 2026-02-25 |
| [Weekly Meeting](https://weekly-meeting-app-vudrpjptuq-uc.a.run.app) | [weekly-meeting-app](https://github.com/S2G-Investments/weekly-meeting-app) | Weekly team meeting app for shared agendas and notes | Chuck | 2026-02-23 |
| [Executive Dashboard](https://s2g-executive-dashboard-vudrpjptuq-uc.a.run.app) | [s2g-dashboard](https://github.com/S2G-Investments/s2g-dashboard) | S2G-wide executive metrics dashboard | Chuck | 2026-02-23 |
| [H1 Goal Dashboard](https://h1-goal-dashboard-vudrpjptuq-uc.a.run.app) | [h1-goal-dashboard](https://github.com/S2G-Investments/h1-goal-dashboard) | H1 2026 strategic goal tracking with AI-powered insights | Chuck | 2026-02-25 |
| [Exit ABC](https://exit-abc-vudrpjptuq-uc.a.run.app) | [Exit-ABC](https://github.com/S2G-Investments/Exit-ABC) | Exit modeling and analysis tool | Chuck | 2026-02-25 |
| [Networker](https://networker-vudrpjptuq-uc.a.run.app) | [networker](https://github.com/S2G-Investments/networker) | Contact relationship management tool | Chuck | 2026-02-27 |
| [Narwhal Tracker](https://narwhal-tracker-vudrpjptuq-uc.a.run.app) | — | Narwhal deal tracking | — | — |
| [Priority Accounts](https://priority-accounts-vudrpjptuq-uc.a.run.app) | — | Priority account management | — | — |
| [Salesforce Login Report](https://salesforce-login-report-vudrpjptuq-uc.a.run.app) | [salesforce-login-report](https://github.com/S2G-Investments/salesforce-login-report) | Salesforce user login activity report | Chuck | 2026-02-25 |
| [SEC MR Dashboard](https://sec-mr-dashboard-vudrpjptuq-uc.a.run.app) | [sec-marketing-review](https://github.com/S2G-Investments/sec-marketing-review) | SEC marketing review compliance dashboard | Chuck | 2026-02-27 |
| [Software Request](https://software-request-app-vudrpjptuq-uc.a.run.app) | [software-request-app](https://github.com/S2G-Investments/software-request-app) | Employee software request portal | Chuck | 2026-02-25 |
| [AI Training](https://s2g-ai-training-vudrpjptuq-uc.a.run.app) | [s2g-ai-training](https://github.com/S2G-Investments/s2g-ai-training) | 10-lesson AI training curriculum for the S2G team | Chuck | 2026-02-19 |

---

## Data Pipelines & Automation

Background services, scheduled jobs, and Salesforce integrations.

| Repo | Description | Owner | Last Updated |
|------|-------------|-------|--------------|
| [origination-gmail-ingest](https://github.com/S2G-Investments/origination-gmail-ingest) | Serverless pipeline: processes origination@ inbox deals via Claude AI → Salesforce | Sean Nguyen | 2026-02-26 |
| [pass-email-ingest](https://github.com/S2G-Investments/pass-email-ingest) | Serverless pipeline: processes pass@ inbox deals via Claude AI → Salesforce | Sean Nguyen | 2025-12-17 |
| [board-deck-gmail-ingest](https://github.com/S2G-Investments/board-deck-gmail-ingest) | Board materials email processor with AI extraction and Box storage | Sean Nguyen | 2025-09-29 |
| [calendar-to-salesforce](https://github.com/S2G-Investments/calendar-to-salesforce) | Google Calendar → Salesforce Event sync for IR team | Sean Nguyen | 2026-01-07 |
| [s2g-zoom-meeting-sync](https://github.com/S2G-Investments/s2g-zoom-meeting-sync) | Zoom transcript pipeline: webhooks → VTT parsing → Box upload → AI processing | Sean Nguyen | 2026-02-26 |
| [fivetran-dbt](https://github.com/S2G-Investments/fivetran-dbt) | dbt project transforming Fivetran source data into analytics tables | Sean Nguyen | 2025-11-13 |
| [slack-time-allocation-bot](https://github.com/S2G-Investments/slack-time-allocation-bot) | Slack DM bot for personal time logging with BigQuery storage | Sean Nguyen | 2026-02-05 |

---

## Dashboards & Reports (Posit Connect)

Deployed to [connect.s2gdata.com](https://connect.s2gdata.com).

| Repo | Description | Owner | Last Updated |
|------|-------------|-------|--------------|
| [s2g-opps-dashboard](https://github.com/S2G-Investments/s2g-opps-dashboard) | Pipeline metrics dashboard, auto-deploys every 6 hours from Salesforce/BigQuery | Sean Nguyen | 2026-02-23 |
| [ir_dashboard](https://github.com/S2G-Investments/ir_dashboard) | IR tracking dashboard — LP meetings and fund pipeline | Sean Nguyen | 2026-02-17 |
| [software-approval-portal](https://github.com/S2G-Investments/software-approval-portal) | Software approval portal for Technology, Legal, and Compliance review | Christopher Marshall | 2026-01-30 |
| [contract-agent](https://github.com/S2G-Investments/contract-agent) | AI-powered legal contract intake application | Sean Nguyen | 2026-01-27 |
| [summit](https://github.com/S2G-Investments/summit) | S2G Summit dashboards — year-in-review analytics | Sean Nguyen | 2026-02-27 |

---

## AI & Tooling

| Repo | Description | Owner | Last Updated |
|------|-------------|-------|--------------|
| [ir-meeting-brief](https://github.com/S2G-Investments/ir-meeting-brief) | AI briefing generator for IR meetings using Calendar, Salesforce, and Gemini | Sean Nguyen | 2026-01-07 |
| [chatgpt-license-audit](https://github.com/S2G-Investments/chatgpt-license-audit) | ChatGPT Team license audit — scores users and recommends keep vs. cycle off | Sean Nguyen | 2026-02-10 |
| [claude-intake-app](https://github.com/S2G-Investments/claude-intake-app) | Claude access application portal for S2G employees | Christopher Marshall | 2026-02-20 |
| [s2g-excalidraw-render](https://github.com/S2G-Investments/s2g-excalidraw-render) | Cloud Run service for rendering Excalidraw diagrams to PNG/SVG | Sean Nguyen | 2026-02-13 |
| [historical-email-interest](https://github.com/S2G-Investments/historical-email-interest) | LP investment interest discovery from email history using Vertex AI RAG | Sean Nguyen | 2026-01-07 |

---

## Configuration & Shared Resources

| Repo | Description | Owner | Last Updated |
|------|-------------|-------|--------------|
| [claude-config](https://github.com/S2G-Investments/claude-config) | Shared Claude Code configuration templates for the S2G team | Sean Nguyen | 2026-01-27 |
| [claude-skills](https://github.com/S2G-Investments/claude-skills) | Claude Code skills for BigQuery, Salesforce, Box, and S2G brand | Christopher Marshall | 2026-01-26 |
| [GCP-Claude-security-settings](https://github.com/S2G-Investments/GCP-Claude-security-settings) | Role-based Claude Code config for S2G multi-user deployment with auditable access controls | Sean Nguyen | 2026-02-27 |

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Next.js (Cloud Run), Streamlit (Posit Connect), Shiny for Python |
| Auth | Google OAuth via NextAuth.js, restricted to @s2ginvestments.com |
| Database | BigQuery (`s2g-data-platform`) |
| CRM | Salesforce (JWT auth via service account) |
| AI | Claude (Anthropic), Gemini (Google), GPT-4o (OpenAI) |
| Storage | Google Drive, Box |
| Infra | GCP Cloud Run, Cloud Build, Secret Manager, Artifact Registry |
| Pipelines | Cloud Run Jobs, Cloud Scheduler, Fivetran + dbt |

---

*To add or update a service listing, edit `profile/README.md` in this repo.*
