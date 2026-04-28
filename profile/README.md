# S2G Investments Engineering

Internal tools, data pipelines, and AI-powered applications built by the S2G team.

**Cloud Run URL pattern:** `https://{service-name}-vudrpjptuq-uc.a.run.app`  
**Posit Connect:** `https://connect.s2gdata.com`  
**GCP Project:** `s2g-data-platform`  
**Last updated:** 2026-04-28 08:45 UTC

---

## Web Apps (Cloud Run)

User-facing applications deployed on Google Cloud Run. All restricted to `@s2ginvestments.com` via Google OAuth.

| App | Repo | Description | Owner | Last Commit | Last Committer |
|-----|------|-------------|-------|-------------|----------------|
| [My Dashboard](https://mydashboard-s2g-vudrpjptuq-uc.a.run.app) | [mydashboard-s2g](https://github.com/S2G-Investments/mydashboard-s2g) | Personal dashboard with notes scratchpad, calendar, and links to all S2G apps | Kevin Lo | 2026-03-10 | Kevin Lo |
| [S2G Notes](https://s2g-notes-vudrpjptuq-uc.a.run.app) | [s2g-notes](https://github.com/S2G-Investments/s2g-notes) | Meeting notes tied to Google Calendar events, with public/private visibility | Chuck | 2026-04-25 | Chuck |
| [Portfolio Companies](https://portfolio-companies-app-vudrpjptuq-uc.a.run.app) | [portfolio-companies-app](https://github.com/S2G-Investments/portfolio-companies-app) | Portfolio company tracker with Salesforce integration and annotations | Chuck | 2026-04-16 | klo-s2g |
| [Portco Quarterly Performance](https://pqp-vudrpjptuq-uc.a.run.app) | [pqp](https://github.com/S2G-Investments/pqp) | Quarterly performance tracking for portfolio companies | Chuck | 2026-04-09 | Sean Nguyen |
| [Weekly Meeting](https://weekly-meeting-app-vudrpjptuq-uc.a.run.app) | [weekly-meeting-app](https://github.com/S2G-Investments/weekly-meeting-app) | Weekly team meeting app for shared agendas and notes | Chuck | 2026-03-19 | Chuck |
| [Executive Dashboard](https://s2g-executive-dashboard-vudrpjptuq-uc.a.run.app) | [s2g-dashboard](https://github.com/S2G-Investments/s2g-dashboard) | S2G-wide executive metrics dashboard | Chuck | 2026-04-09 | Sean Nguyen |
| [H1 Goal Dashboard](https://h1-goal-dashboard-vudrpjptuq-uc.a.run.app) | [h1-goal-dashboard](https://github.com/S2G-Investments/h1-goal-dashboard) | H1 2026 strategic goal tracking with AI-powered insights | Chuck | 2026-04-21 | Sean Nguyen |
| [Exit ABC](https://exit-abc-vudrpjptuq-uc.a.run.app) | [Exit-ABC](https://github.com/S2G-Investments/Exit-ABC) | Exit modeling and analysis tool | Chuck | 2026-03-20 | Chuck |
| [Networker](https://networker-vudrpjptuq-uc.a.run.app) | [networker](https://github.com/S2G-Investments/networker) | Contact relationship management tool | Chuck | 2026-04-28 | Chuck |
| [Narwhal Tracker](https://narwhal-tracker-vudrpjptuq-uc.a.run.app) | — | Narwhal deal tracking | — | — | — |
| [Priority Accounts](https://priority-accounts-vudrpjptuq-uc.a.run.app) | — | Priority account management | — | — | — |
| [Salesforce Login Report](https://salesforce-login-report-vudrpjptuq-uc.a.run.app) | [salesforce-login-report](https://github.com/S2G-Investments/salesforce-login-report) | Salesforce user login activity report | Chuck | 2026-03-01 | Chuck |
| [SEC MR Dashboard](https://sec-mr-dashboard-vudrpjptuq-uc.a.run.app) | [sec-marketing-review](https://github.com/S2G-Investments/sec-marketing-review) | SEC marketing review compliance dashboard | Chuck | 2026-04-09 | Sean Nguyen |
| [Software Request](https://software-request-app-vudrpjptuq-uc.a.run.app) | [software-request-app](https://github.com/S2G-Investments/software-request-app) | Employee software request portal | Chuck | 2026-03-14 | Chuck |
| [AI Training](https://s2g-ai-training-vudrpjptuq-uc.a.run.app) | [s2g-ai-training](https://github.com/S2G-Investments/s2g-ai-training) | 10-lesson AI training curriculum for the S2G team | Chuck | 2026-04-04 | Chuck |
| [Summit Tables](https://summit-tables-vudrpjptuq-uc.a.run.app) | [Summit_Tables](https://github.com/S2G-Investments/Summit_Tables) | Intelligent seating management tool for S2G Annual Summit events | Mitch Worden | 2026-04-28 | Sean Nguyen |
| [Feedback Window](https://feedback-window-vudrpjptuq-uc.a.run.app) | [feedback-window](https://github.com/S2G-Investments/feedback-window) | Embeddable feedback widget and admin dashboard for collecting user feedback from S2G apps | Chuck | 2026-03-12 | Chuck |

---

## Data Pipelines & Automation

Background services, scheduled jobs, and Salesforce integrations.

| Repo | Description | Owner | Last Commit | Last Committer |
|------|-------------|-------|-------------|----------------|
| [origination-gmail-ingest](https://github.com/S2G-Investments/origination-gmail-ingest) | Serverless pipeline: processes origination@ inbox deals via Claude AI → Salesforce | Sean Nguyen | 2026-04-21 | Sean Nguyen |
| [pass-email-ingest](https://github.com/S2G-Investments/pass-email-ingest) | Serverless pipeline: processes pass@ inbox deals via Claude AI → Salesforce | Sean Nguyen | 2026-04-09 | Sean Nguyen |
| [board-deck-gmail-ingest](https://github.com/S2G-Investments/board-deck-gmail-ingest) | Board materials email processor with AI extraction and Box storage | Sean Nguyen | 2026-04-09 | Sean Nguyen |
| [calendar-to-salesforce](https://github.com/S2G-Investments/calendar-to-salesforce) | Google Calendar → Salesforce Event sync for IR team | Sean Nguyen | 2026-01-07 | Sean Nguyen |
| [s2g-zoom-meeting-sync](https://github.com/S2G-Investments/s2g-zoom-meeting-sync) | Zoom transcript pipeline: webhooks → VTT parsing → Box upload → AI processing | Sean Nguyen | 2026-04-02 | Sean Nguyen |
| [fivetran-dbt](https://github.com/S2G-Investments/fivetran-dbt) | dbt project transforming Fivetran source data into analytics tables | Joe Intrakamhang | 2026-04-16 | Sean Nguyen |
| [slack-time-allocation-bot](https://github.com/S2G-Investments/slack-time-allocation-bot) | Slack DM bot for personal time logging with BigQuery storage | Sean Nguyen | 2026-02-05 | Sean Nguyen |
| [s2g-notes-ingest](https://github.com/S2G-Investments/s2g-notes-ingest) | Ingests and processes S2G meeting notes, syncing data to BigQuery | Sean Nguyen | 2026-04-15 | Sean Nguyen |
| [salesforce-login-sync](https://github.com/S2G-Investments/salesforce-login-sync) | Daily Cloud Function syncing Salesforce user login activity to BigQuery | Chuck | 2026-03-13 | Chuck |

---

## Dashboards & Reports (Posit Connect)

Deployed to [connect.s2gdata.com](https://connect.s2gdata.com).

| Repo | Description | Owner | Last Commit | Last Committer |
|------|-------------|-------|-------------|----------------|
| [s2g-opps-dashboard](https://github.com/S2G-Investments/s2g-opps-dashboard) | Pipeline metrics dashboard, auto-deploys every 6 hours from Salesforce/BigQuery | Sean Nguyen | 2026-04-23 | Sean Nguyen |
| [ir_dashboard](https://github.com/S2G-Investments/ir_dashboard) | IR tracking dashboard — LP meetings and fund pipeline | Sean Nguyen | 2026-02-17 | Sean Nguyen |
| [software-approval-portal](https://github.com/S2G-Investments/software-approval-portal) | Software approval portal for Technology, Legal, and Compliance review | Christopher Marshall | 2026-01-30 | Christopher Marshall |
| [contract-agent](https://github.com/S2G-Investments/contract-agent) | AI-powered legal contract intake application | Sean Nguyen | 2026-01-27 | Sean Nguyen |
| [summit](https://github.com/S2G-Investments/summit) | S2G Summit dashboards — year-in-review analytics | Sean Nguyen | 2026-04-27 | Sean Nguyen |
| [fv-staffing-tool](https://github.com/S2G-Investments/fv-staffing-tool) | Streamlit app for tracking and managing FV staffing assignments | Sean Nguyen | 2026-03-30 | Francis Villante |
| [meeting-capture-scorecard](https://github.com/S2G-Investments/meeting-capture-scorecard) | Scores meeting capture coverage against Google Calendar, deployed to Posit Connect | Christopher Marshall | 2026-04-12 | Sean Nguyen |

---

## AI & Tooling

| Repo | Description | Owner | Last Commit | Last Committer |
|------|-------------|-------|-------------|----------------|
| [ir-meeting-brief](https://github.com/S2G-Investments/ir-meeting-brief) | AI briefing generator for IR meetings using Calendar, Salesforce, and Gemini | Sean Nguyen | 2026-03-19 | Sean Nguyen |
| [chatgpt-license-audit](https://github.com/S2G-Investments/chatgpt-license-audit) | ChatGPT Team license audit — scores users and recommends keep vs. cycle off | Sean Nguyen | 2026-03-25 | Sean Nguyen |
| [claude-intake-app](https://github.com/S2G-Investments/claude-intake-app) | Claude access application portal for S2G employees | Christopher Marshall | 2026-02-20 | Christopher Marshall |
| [s2g-excalidraw-render](https://github.com/S2G-Investments/s2g-excalidraw-render) | Cloud Run service for rendering Excalidraw diagrams to PNG/SVG | Sean Nguyen | 2026-02-14 | Sean Nguyen |
| [historical-email-interest](https://github.com/S2G-Investments/historical-email-interest) | LP investment interest discovery from email history using Vertex AI RAG | Sean Nguyen | 2026-01-07 | Sean Nguyen |

---

## Configuration & Shared Resources

| Repo | Description | Owner | Last Commit | Last Committer |
|------|-------------|-------|-------------|----------------|
| [claude-config](https://github.com/S2G-Investments/claude-config) | Shared Claude Code configuration templates for the S2G team | Sean Nguyen | 2026-01-27 | Sean Nguyen |
| [claude-skills](https://github.com/S2G-Investments/claude-skills) | Claude Code skills for BigQuery, Salesforce, Box, and S2G brand | Sean Nguyen | 2026-01-26 | Christopher Marshall |
| [GCP-Claude-security-settings](https://github.com/S2G-Investments/GCP-Claude-security-settings) | Role-based Claude Code config for S2G multi-user deployment with auditable access controls | Sean Nguyen | 2026-04-28 | Sean Nguyen |

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

## How This Works

This README is auto-generated daily at midnight PT by a GitHub Actions workflow.

- **`services.json`** — the editable source of truth. When you add a new app, add an entry here.
- **`scripts/update_readme.py`** — queries the GitHub API for each repo's last commit date + author, then regenerates this file.
- **`.github/workflows/update-readme.yml`** — runs at midnight PT every day, or on-demand via `gh workflow run update-readme.yml --repo S2G-Investments/.github`.

The workflow only commits if data actually changed, so there are no noisy empty commits on quiet days.

> **Note:** The "Last Commit" and "Last Committer" columns require an `ORG_PAT` secret with `repo` scope to read cross-repo commit data. Without it, these columns show `—`.
