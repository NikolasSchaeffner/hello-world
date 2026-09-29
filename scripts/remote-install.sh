#!/usr/bin/env bash
set -euo pipefail

# ---------------------------------------------------------------------------
# Hello World Skill + Subagents — Remote Installer
# Installs the /hello command and a curated set of Claude Code subagents.
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/nikolasschaeffner/hello-world/main/scripts/remote-install.sh | bash -s -- --user
#   curl -fsSL https://raw.githubusercontent.com/nikolasschaeffner/hello-world/main/scripts/remote-install.sh | bash -s -- --project
#   curl -fsSL https://raw.githubusercontent.com/nikolasschaeffner/hello-world/main/scripts/remote-install.sh | bash -s -- --desktop
# ---------------------------------------------------------------------------

# Branch or tag to install from (override with HELLO_WORLD_REF=<branch>)
REPO_REF="${HELLO_WORLD_REF:-main}"
REPO_RAW="https://raw.githubusercontent.com/nikolasschaeffner/hello-world/${REPO_REF}"
SKILL_NAME="hello-world"
COMMAND_FILES=("hello.md")

# Curated subagents from VoltAgent/awesome-claude-code-subagents (MIT, see .claude/agents/LICENSE-VoltAgent)
AGENT_FILES=(
  "java-architect.md" "code-reviewer.md" "architect-reviewer.md" "qa-expert.md"
  "debugger.md" "refactoring-specialist.md" "test-automator.md"
  "documentation-engineer.md" "technical-writer.md"
  "competitive-analyst.md" "business-analyst.md" "market-researcher.md" "research-analyst.md"
  "fintech-engineer.md" "risk-manager.md" "microservices-architect.md"
)

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; CYAN='\033[0;36m'; NC='\033[0m'
info()    { echo -e "${CYAN}[hello-world]${NC} $*"; }
success() { echo -e "${GREEN}[hello-world]${NC} $*"; }
warn()    { echo -e "${YELLOW}[hello-world]${NC} $*"; }
error()   { echo -e "${RED}[hello-world]${NC} $*" >&2; exit 1; }

# ---- dependency check -------------------------------------------------------
require_cmd() {
  command -v "$1" &>/dev/null || error "Required command '$1' not found. Please install it and retry."
}
require_cmd curl

# ---- download helper --------------------------------------------------------
fetch() {
  local url="$1" dest="$2"
  curl -fsSL "$url" -o "$dest" || error "Failed to download: $url"
}

# ---- shared install step -----------------------------------------------------
# $1 = base directory that receives commands/ and agents/ (e.g. ~/.claude)
install_into() {
  local base="$1"
  mkdir -p "$base/commands" "$base/agents"
  info "Installing commands to: $base/commands"
  for file in "${COMMAND_FILES[@]}"; do
    fetch "$REPO_RAW/.claude/commands/$file" "$base/commands/$file"
    success "Installed command $file"
  done
  info "Installing ${#AGENT_FILES[@]} subagents to: $base/agents"
  for file in "${AGENT_FILES[@]}"; do
    fetch "$REPO_RAW/.claude/agents/$file" "$base/agents/$file"
    success "Installed agent ${file%.md}"
  done
}

# ---- installation modes -----------------------------------------------------
install_user() {
  install_into "$HOME/.claude"
  success "Done! Restart Claude Code, then run /hello or /agents to see the subagents."
}

install_project() {
  install_into "./.claude"
  success "Done! Restart Claude Code in this project, then run /hello or /agents."
}

install_desktop() {
  local zip_dir="${TMPDIR:-/tmp}/hello-world-skill-$$"
  local zip_dest="$HOME/Downloads/${SKILL_NAME}.zip"
  mkdir -p "$zip_dir/.claude/commands" "$zip_dir/.claude/agents"

  info "Building zip package for Claude Desktop / Web..."

  for file in "${COMMAND_FILES[@]}"; do
    fetch "$REPO_RAW/.claude/commands/$file" "$zip_dir/.claude/commands/$file"
  done
  for file in "${AGENT_FILES[@]}"; do
    fetch "$REPO_RAW/.claude/agents/$file" "$zip_dir/.claude/agents/$file"
  done

  fetch "$REPO_RAW/SKILL.md"   "$zip_dir/SKILL.md"   2>/dev/null || true
  fetch "$REPO_RAW/README.md"  "$zip_dir/README.md"  2>/dev/null || true

  require_cmd zip
  mkdir -p "$HOME/Downloads"
  (cd "$zip_dir" && zip -r "$zip_dest" .) >/dev/null
  rm -rf "$zip_dir"

  success "Package saved to: $zip_dest"
  info "Upload it in Claude Desktop: Settings → Integrations → Add skill."
}

# ---- interactive mode (TTY) --------------------------------------------------
interactive_mode() {
  echo ""
  echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
  echo -e "${CYAN}  Hello World Skill Installer${NC}"
  echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
  echo ""
  echo "Where would you like to install?"
  echo "  1) User  — ~/.claude/  (available in all projects)"
  echo "  2) Project — ./.claude/  (current directory only)"
  echo "  3) Desktop/Web — download a zip to ~/Downloads/"
  echo ""
  read -rp "Choice [1]: " choice
  choice="${choice:-1}"
  case "$choice" in
    1) install_user ;;
    2) install_project ;;
    3) install_desktop ;;
    *) error "Invalid choice: $choice" ;;
  esac
}

# ---- argument parsing -------------------------------------------------------
MODE=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --user)    MODE="user" ;;
    --project) MODE="project" ;;
    --desktop) MODE="desktop" ;;
    -h|--help)
      echo "Usage: $0 [--user|--project|--desktop]"
      exit 0 ;;
    *) error "Unknown argument: $1. Use --user, --project, or --desktop." ;;
  esac
  shift
done

# ---- dispatch ---------------------------------------------------------------
if [[ -n "$MODE" ]]; then
  case "$MODE" in
    user)    install_user ;;
    project) install_project ;;
    desktop) install_desktop ;;
  esac
elif [[ -t 0 ]]; then
  interactive_mode
else
  # Non-interactive, no flag: default to user install
  warn "No mode specified; defaulting to --user install."
  install_user
fi
