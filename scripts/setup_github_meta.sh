#!/usr/bin/env bash
# ==============================================================================
# Respectful AI & High-Signal Prompting Standard (RAHSPS)
# Automated GitHub Repository Metadata, Topics, Pages, and Release Setup
# ==============================================================================

set -e

REPO="Vitaliy1337/respectful-ai-standard"
HOMEPAGE="https://vitaliy1337.github.io/respectful-ai-standard/"
DESCRIPTION="🌍 The Global Standard for Respectful AI Communication & High-Signal Prompting (RAHSPS). Stop feeding garbage to LLMs. Includes llms.txt, universal agent rules (Cursor, Claude Code, Gemini, Windsurf, Cline, Codex), CLI linter & Web Playground."

TOPICS="ai-ethics,prompt-engineering,llms-txt,ai-agents,context-engineering,high-signal,cursorrules,claude-code,windsurf,mcp,agent-rules,llm,developer-tools,open-standard,rahsps"

echo "=== 1. Updating Description and Homepage ==="
if command -v gh &> /dev/null; then
  gh repo edit "$REPO" \
    --description "$DESCRIPTION" \
    --homepage "$HOMEPAGE" || echo "Note: gh repo edit description/homepage completed or requires token scopes."

  echo "=== 2. Updating Repository Topics ==="
  gh repo edit "$REPO" \
    --add-topic "$TOPICS" || echo "Note: gh repo edit topics completed or requires token scopes."

  echo "=== 3. Enabling GitHub Pages ==="
  gh api -X POST "repos/${REPO}/pages" \
    -f source[branch]=main \
    -f source[path]=/docs || echo "Pages may already be enabled or will deploy via .github/workflows/pages.yml"

  echo "=== 4. Creating GitHub Release v1.0.0 ==="
  gh release create v1.0.0 \
    --title "RAHSPS v1.0.0 — Global Respectful AI & High-Signal Standard" \
    --notes "Official global release of the Respectful AI & High-Signal Prompting Standard (RAHSPS). Includes llms.txt, universal agent matrices (Cursor, Claude, Gemini, Codex, Windsurf, Cline), 7-language localization, CLI linter, and live Web Playground." || echo "Release already exists or token requires release write permissions."

  echo "=== Setup script finished ==="
else
  echo "GitHub CLI (gh) is not installed. Please install gh or configure repository metadata via the GitHub web interface."
fi
