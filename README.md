# S2G-Investments/.github

GitHub organization profile repo for S2G Investments. A daily workflow generates `profile/README.md` — the page shown at [github.com/S2G-Investments](https://github.com/S2G-Investments) — with a live directory of all S2G repos, their owners, and last-commit data.

## File structure

```
services.json                      # Source of truth — add/edit services here
scripts/update_readme.py           # Reads services.json + GitHub API → writes profile/README.md
profile/README.md                  # Auto-generated org profile (do not edit by hand)
.github/workflows/update-readme.yml  # Daily cron + manual trigger
```

## Adding a new service

1. Edit `services.json` — add an entry to the appropriate section (`web_apps`, `pipelines`, `posit_connect`, `ai_tooling`, or `config`).
2. Commit and push. The workflow runs nightly at midnight PT and will pick it up, or trigger it manually:

```bash
gh workflow run update-readme.yml --repo S2G-Investments/.github
```

## Setup: `ORG_PAT` secret

The workflow needs read access to other org repos to fetch last-commit data. The default `GITHUB_TOKEN` is scoped only to this repo, so you must provide a broader token:

1. Create a GitHub **Personal Access Token (classic)** with `repo` scope — or a fine-grained token with read access to all S2G-Investments repos.
2. Add it as a repository secret named **`ORG_PAT`** in this repo's settings (`Settings → Secrets and variables → Actions`).

Without `ORG_PAT`, the "Last Commit" and "Last Committer" columns will show `—`.
