#!/bin/bash
# Full publish flow — run this before pushing docs/ to GitHub.
# Run from dev/
set -e

echo "▶ Building site with absolute URLs..."
uv run pelican -s publishconf.py

echo "▶ Appending GenAiGuidebook URLs to sitemap..."
uv run python append_guidebook_sitemap.py

echo ""
echo "✅ docs/ is ready. Review then push:"
echo "   cd .. && git add docs/ && git commit -m 'publish' && git push"
