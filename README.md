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

The installer also copies 16 curated subagents into `agents/` (from
[VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents), MIT licensed,
see `.claude/agents/LICENSE-VoltAgent`). After a restart, list them with `/agents`.

| Area | Agents |
|------|--------|
| Java & code quality | `java-architect`, `code-reviewer`, `architect-reviewer`, `qa-expert`, `debugger`, `refactoring-specialist`, `test-automator` |
| Documentation | `documentation-engineer`, `technical-writer` |
| Business & research | `competitive-analyst`, `business-analyst`, `market-researcher`, `research-analyst` |
| Domain / architecture | `fintech-engineer`, `risk-manager`, `microservices-architect` |

Claude Code on the web picks up the agents automatically from `.claude/agents/` whenever a session uses this repository.

To install from a branch other than `main`, set `HELLO_WORLD_REF`:

```bash
curl -fsSL https://raw.githubusercontent.com/nikolasschaeffner/hello-world/main/scripts/remote-install.sh | HELLO_WORLD_REF=my-branch bash -s -- --user
```
