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
