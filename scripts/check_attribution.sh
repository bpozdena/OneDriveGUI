#!/bin/sh
# Fails when any commit message in the given range carries AI-tool attribution
# (Co-authored-by / Generated-with / session trailers for Claude, Copilot,
# Cursor, ChatGPT, etc.). GitHub counts those trailer emails as contributors,
# so the trailers show up as tool ads in the Contributors graph.
#
# Usage: check_attribution.sh <git-rev-range>
set -e

RANGE="$1"
if [ -z "$RANGE" ]; then
    echo "usage: $0 <rev-range>" >&2
    exit 2
fi

# Trailer-shaped lines only (anchored at line start), so prose that merely
# mentions a tool is not affected.
PATTERN='^(co-authored-by|co-authored|signed-off-by|assisted-by):.*(anthropic|claude|openai|chatgpt|gpt-[0-9]|copilot|cursor|devin|windsurf|cline|aider|codex|gemini|lovable|v0\.dev|trae|kiro|tabnine|codeium|amazon ?q|qoder|replit|lingma|jetbrains[- ]ai|qwen|deepseek|grok|llm)'
FOOTER='^(generated with|written up with help from)( \[?[A-Za-z0-9. -]+( code| agent| ai)?\]?)?( by .*)?$'
SESSION='^(claude-session|AIGC-|AI-assisted)'

if ! git rev-list -n 1 "$RANGE" >/dev/null 2>&1; then
    # Force-pushes make before..after ranges invalid; fall back to recent tip.
    RANGE="HEAD~50..HEAD"
fi

found=0
for c in $(git rev-list "$RANGE"); do
    msg=$(git log -1 --format=%B "$c")
    hits=$(printf '%s\n' "$msg" | grep -iE "$PATTERN" || true)
    if [ -z "$hits" ]; then
        # "Generated with [Claude Code]" style footers: require a tool name
        hits=$(printf '%s\n' "$msg" | grep -iE "$FOOTER" | grep -iE 'claude|gpt|openai|copilot|cursor|devin|windsurf|cline|aider|gemini|lovable|copilot' || true)
    fi
    if [ -z "$hits" ]; then
        hits=$(printf '%s\n' "$msg" | grep -iE "$SESSION" || true)
    fi
    if [ -n "$hits" ]; then
        echo "::error::commit $c carries AI attribution"
        printf '%s\n' "$hits" | sed 's/^/    /'
        found=1
    fi
done

if [ "$found" -ne 0 ]; then
    echo "AI-tool attribution trailers found. Remove the Co-authored-by /"
    echo "Generated-with / session lines from the commit messages and push again."
    exit 1
fi

echo "No AI attribution trailers found."
