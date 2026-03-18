#!/usr/bin/env python3
"""
Regenerates profile/README.md from services.json + live GitHub API data.
Fetches last commit date and author for each repo.
"""

import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

ORG = "S2G-Investments"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
ROOT = Path(__file__).parent.parent


def github_get(path: str) -> dict | None:
    url = f"https://api.github.com{path}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    })
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"  WARNING: GitHub API {path} → {e.code}", file=sys.stderr)
        return None


def get_last_commit(repo: str) -> tuple[str, str]:
    """Returns (date YYYY-MM-DD, author name) for the latest commit."""
    data = github_get(f"/repos/{ORG}/{repo}/commits?per_page=1")
    if not data or not isinstance(data, list) or len(data) == 0:
        return "—", "—"
    commit = data[0]
    author_name = (
        commit.get("commit", {}).get("author", {}).get("name")
        or commit.get("author", {}).get("login")
        or "—"
    )
    date_str = commit.get("commit", {}).get("author", {}).get("date", "")
    if date_str:
        date_str = date_str[:10]  # YYYY-MM-DD
    else:
        date_str = "—"
    return date_str, author_name


def normalize_author(name: str) -> str:
    mapping = {
        "chuck-coder": "Chuck",
        "sean-S2G": "Sean Nguyen",
        "Chris-S2Gmaker": "Christopher Marshall",
        "Kevin": "Kevin Lo",
    }
    return mapping.get(name, name)


def repo_link(repo: str) -> str:
    return f"[{repo}](https://github.com/{ORG}/{repo})"


def build_readme(services: dict, commit_cache: dict) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# S2G Investments Engineering",
        "",
        "Internal tools, data pipelines, and AI-powered applications built by the S2G team.",
        "",
        f"**Cloud Run URL pattern:** `https://{{service-name}}-vudrpjptuq-uc.a.run.app`  ",
        "**Posit Connect:** `https://connect.s2gdata.com`  ",
        "**GCP Project:** `s2g-data-platform`  ",
        f"**Last updated:** {now}",
        "",
        "---",
        "",
        "## Web Apps (Cloud Run)",
        "",
        "User-facing applications deployed on Google Cloud Run. All restricted to `@s2ginvestments.com` via Google OAuth.",
        "",
        "| App | Repo | Description | Owner | Last Commit | Last Committer |",
        "|-----|------|-------------|-------|-------------|----------------|",
    ]

    for app in services["web_apps"]:
        repo = app["repo"]
        if repo:
            date, author = commit_cache.get(repo, ("—", "—"))
            author = normalize_author(author)
            repo_col = repo_link(repo)
        else:
            date, author = "—", "—"
            repo_col = "—"
        name_col = f"[{app['name']}]({app['url']})"
        lines.append(f"| {name_col} | {repo_col} | {app['description']} | {app['owner']} | {date} | {author} |")

    lines += [
        "",
        "---",
        "",
        "## Data Pipelines & Automation",
        "",
        "Background services, scheduled jobs, and Salesforce integrations.",
        "",
        "| Repo | Description | Owner | Last Commit | Last Committer |",
        "|------|-------------|-------|-------------|----------------|",
    ]

    for svc in services["pipelines"]:
        repo = svc["repo"]
        date, author = commit_cache.get(repo, ("—", "—"))
        author = normalize_author(author)
        lines.append(f"| {repo_link(repo)} | {svc['description']} | {svc['owner']} | {date} | {author} |")

    lines += [
        "",
        "---",
        "",
        "## Dashboards & Reports (Posit Connect)",
        "",
        f"Deployed to [connect.s2gdata.com](https://connect.s2gdata.com).",
        "",
        "| Repo | Description | Owner | Last Commit | Last Committer |",
        "|------|-------------|-------|-------------|----------------|",
    ]

    for svc in services["posit_connect"]:
        repo = svc["repo"]
        date, author = commit_cache.get(repo, ("—", "—"))
        author = normalize_author(author)
        lines.append(f"| {repo_link(repo)} | {svc['description']} | {svc['owner']} | {date} | {author} |")

    lines += [
        "",
        "---",
        "",
        "## AI & Tooling",
        "",
        "| Repo | Description | Owner | Last Commit | Last Committer |",
        "|------|-------------|-------|-------------|----------------|",
    ]

    for svc in services["ai_tooling"]:
        repo = svc["repo"]
        date, author = commit_cache.get(repo, ("—", "—"))
        author = normalize_author(author)
        lines.append(f"| {repo_link(repo)} | {svc['description']} | {svc['owner']} | {date} | {author} |")

    lines += [
        "",
        "---",
        "",
        "## Configuration & Shared Resources",
        "",
        "| Repo | Description | Owner | Last Commit | Last Committer |",
        "|------|-------------|-------|-------------|----------------|",
    ]

    for svc in services["config"]:
        repo = svc["repo"]
        date, author = commit_cache.get(repo, ("—", "—"))
        author = normalize_author(author)
        lines.append(f"| {repo_link(repo)} | {svc['description']} | {svc['owner']} | {date} | {author} |")

    lines += [
        "",
        "---",
        "",
        "## Tech Stack",
        "",
        "| Layer | Technology |",
        "|-------|------------|",
        "| Frontend | Next.js (Cloud Run), Streamlit (Posit Connect), Shiny for Python |",
        "| Auth | Google OAuth via NextAuth.js, restricted to @s2ginvestments.com |",
        "| Database | BigQuery (`s2g-data-platform`) |",
        "| CRM | Salesforce (JWT auth via service account) |",
        "| AI | Claude (Anthropic), Gemini (Google), GPT-4o (OpenAI) |",
        "| Storage | Google Drive, Box |",
        "| Infra | GCP Cloud Run, Cloud Build, Secret Manager, Artifact Registry |",
        "| Pipelines | Cloud Run Jobs, Cloud Scheduler, Fivetran + dbt |",
        "",
        "---",
        "",
        "## How This Works",
        "",
        "This README is auto-generated daily at midnight PT by a GitHub Actions workflow.",
        "",
        "- **`services.json`** — the editable source of truth. When you add a new app, add an entry here.",
        "- **`scripts/update_readme.py`** — queries the GitHub API for each repo's last commit date + author, then regenerates this file.",
        "- **`.github/workflows/update-readme.yml`** — runs at midnight PT every day, or on-demand via `gh workflow run update-readme.yml --repo S2G-Investments/.github`.",
        "",
        "The workflow only commits if data actually changed, so there are no noisy empty commits on quiet days.",
        "",
        "> **Note:** The \"Last Commit\" and \"Last Committer\" columns require an `ORG_PAT` secret with `repo` scope to read cross-repo commit data. Without it, these columns show `—`.",
    ]

    return "\n".join(lines) + "\n"


def main():
    services_path = ROOT / "services.json"
    readme_path = ROOT / "profile" / "README.md"

    with open(services_path) as f:
        services = json.load(f)

    # Collect all unique repos
    all_repos = set()
    for section in services.values():
        for svc in section:
            if svc.get("repo"):
                all_repos.add(svc["repo"])

    print(f"Fetching commit data for {len(all_repos)} repos...")
    commit_cache = {}
    for repo in sorted(all_repos):
        print(f"  {repo}...", end=" ", flush=True)
        date, author = get_last_commit(repo)
        commit_cache[repo] = (date, author)
        print(f"{date} by {author}")

    readme = build_readme(services, commit_cache)
    readme_path.write_text(readme)
    print(f"\nWrote {readme_path}")


if __name__ == "__main__":
    main()
