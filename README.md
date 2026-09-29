# hello-world

A minimal Claude Code skill demonstrating remote installation.

## Quick install

**User-level** (all projects):
```bash
curl -fsSL https://raw.githubusercontent.com/nikolasschaeffner/hello-world/main/scripts/remote-install.sh | bash -s -- --user
```

**Project-level** (current directory only):
```bash
curl -fsSL https://raw.githubusercontent.com/nikolasschaeffner/hello-world/main/scripts/remote-install.sh | bash -s -- --project
```

**Claude Desktop / Web** (downloads a zip):
```bash
curl -fsSL https://raw.githubusercontent.com/nikolasschaeffner/hello-world/main/scripts/remote-install.sh | bash -s -- --desktop
```

## What it installs

| Command | Description |
|---------|-------------|
| `/hello` | Greet the user and offer help |

### Subagents

The installer also copies **137 subagents** into `agents/`, taken from
[VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents)
(commit `82b7382`, MIT licensed, see `.claude/agents/LICENSE-VoltAgent`). The full list is in
`.claude/agents/agents.txt`. After a restart, browse them with `/agents`.

| Area | Examples |
|------|----------|
| Core & languages | `backend-developer`, `fullstack-developer`, `java-architect`, `python-pro`, `typescript-pro`, `spring-boot-engineer`, `sql-pro` |
| Infrastructure | `cloud-architect`, `docker-expert`, `kubernetes-specialist`, `terraform-engineer`, `security-engineer` |
| Quality & security | `code-reviewer`, `architect-reviewer`, `qa-expert`, `debugger`, `security-auditor`, `penetration-tester` |
| Data & AI | `data-scientist`, `data-analyst`, `llm-architect`, `prompt-engineer`, `machine-learning-engineer` |
| Developer experience | `refactoring-specialist`, `documentation-engineer`, `git-workflow-manager`, `mcp-developer` |
| Specialized domains | `fintech-engineer`, `risk-manager`, `game-developer`, `payment-integration`, `seo-specialist` |
| Business & product | `business-analyst`, `product-manager`, `project-manager`, `technical-writer`, `legal-advisor` |
| Planning & research | `agent-organizer`, `multi-agent-coordinator`, `research-analyst`, `market-researcher`, `competitive-analyst` |

**Deliberately left out (24):**

- Unsafe: `agent-installer` (installs further unreviewed agents), `healthcare-admin` (`curl | bash` from a third party), `content-quality-editor` (installs an npm package globally on its own).
- Depend on tools that do not exist in this setup: `codebase-orchestrator`, `visual-asset-generator`.
- Duplicates: `ml-engineer`, `mobile-developer`, `devops-incident-responder`.
- Infrastructure for multi-agent file state, or overlapping with Claude Code's built-in memory: `context-manager`, `error-coordinator`, `performance-monitor`, `task-distributor`, `memory-curator`.
- Windows / Microsoft administration and US healthcare regulation: `powershell-5.1-expert`, `powershell-7-expert`, `powershell-module-architect`, `powershell-ui-architect`, `powershell-security-hardening`, `ad-security-reviewer`, `windows-infra-admin`, `m365-admin`, `it-ops-orchestrator`, `dotnet-framework-4.8-expert`, `hipaa-compliance`.

Claude Code on the web picks up the agents automatically from `.claude/agents/` whenever a session uses this repository.

To install from a branch other than `main`, set `HELLO_WORLD_REF`:

```bash
curl -fsSL https://raw.githubusercontent.com/nikolasschaeffner/hello-world/main/scripts/remote-install.sh | HELLO_WORLD_REF=my-branch bash -s -- --user
```
