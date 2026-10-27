#!/usr/bin/env bash
# ==============================================================================
# Respectful AI & High-Signal Prompting Standard (RAHSPS) — Universal Installer
# One-command drop-in rulebook generator for all major AI coding environments.
# Usage:
#   curl -sSL https://raw.githubusercontent.com/Vitaliy1337/respectful-ai-standard/main/install.sh | bash
#   or locally: ./install.sh [--all]
# ==============================================================================

set -e

# Terminal colors
BOLD="\033[1m"
GREEN="\033[32m"
BLUE="\033[34m"
CYAN="\033[36m"
YELLOW="\033[33m"
RESET="\033[0m"

REPO_BASE="https://raw.githubusercontent.com/Vitaliy1337/respectful-ai-standard/main"

echo -e "${BOLD}${CYAN}======================================================================${RESET}"
echo -e "${BOLD}${CYAN}   RESPECTFUL AI & HIGH-SIGNAL STANDARD (RAHSPS) — INSTALLER v3.0    ${RESET}"
echo -e "${BOLD}${CYAN}======================================================================${RESET}"
echo -e "Target Directory: ${BOLD}$(pwd)${RESET}\n"

FILES=(
  "AGENTS.md"
  "CLAUDE.md"
  "GEMINI.md"
  ".cursorrules"
  ".windsurfrules"
  ".clinerules"
)

# Function to download or copy locally
install_file() {
  local filename="$1"
  echo -ne "Installing ${BOLD}${filename}${RESET}... "

  if [ -f "$(dirname "$0")/${filename}" ]; then
    # Local installation from cloned repo
    cp "$(dirname "$0")/${filename}" "./${filename}"
    echo -e "${GREEN}✔ Installed (local)${RESET}"
  else
    # Remote installation via curl
    if curl -sSL -f "${REPO_BASE}/${filename}" -o "./${filename}"; then
      echo -e "${GREEN}✔ Downloaded${RESET}"
    else
      echo -e "${YELLOW}⚠ Failed to fetch ${filename}${RESET}"
    fi
  fi
}

for f in "${FILES[@]}"; do
  install_file "$f"
done

echo -e "\n${BOLD}${GREEN}✔ SUCCESS! All Respect & Signal Gate rulebooks have been injected.${RESET}"
echo -e "Supported IDEs & Agents configured:"
echo -e "  • ${CYAN}AGENTS.md${RESET}      → Roo Code, OpenCode, Codex, Devin, Custom Subagents"
echo -e "  • ${CYAN}CLAUDE.md${RESET}      → Anthropic Claude Code CLI"
echo -e "  • ${CYAN}GEMINI.md${RESET}      → Google Gemini CLI & Antigravity"
echo -e "  • ${CYAN}.cursorrules${RESET}   → Cursor IDE Composer & Agent Mode"
echo -e "  • ${CYAN}.windsurfrules${RESET} → Windsurf Cascade"
echo -e "  • ${CYAN}.clinerules${RESET}    → Cline / Roo Code (VS Code)"

echo -e "\n${BOLD}Next steps:${RESET}"
echo -e "  1. Start prompts with: ${BOLD}«Уважаемый агент...»${RESET} or ${BOLD}«Respected Agent...»${RESET}"
echo -e "  2. Test prompt quality with CLI: ${CYAN}pip install -e . && respect-lint \"...\"${RESET}"
echo -e "  3. Explore interactive Web Playground: ${CYAN}https://vitaliy1337.github.io/respectful-ai-standard/${RESET}\n"
