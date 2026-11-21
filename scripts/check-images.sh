#!/usr/bin/env bash
# Flag images that are too heavy for a document repository.
#
# Read-only. Two hard checks and one report:
#   1. size     a file over MAX_BYTES fails
#   2. pixels   a long edge over MAX_EDGE fails
#   3. orphans  an image that no tracked text file mentions (report, --all only)
#
# The default scope is what is staged: images added in the index. That is the
# moment the cost can still be avoided. --all audits the whole imgs/ tree,
# including files that predate this rule, which is why it is not the default.
#
# Fixes: a photograph belongs in JPEG q85, not PNG (measured 4.39 MB -> 0.46 MB
# at 1920x1276). Flat art, a table or a UI screenshot stays PNG but wants
# -strip -colors 64. Never rename an image that is already published: Medium's
# hosted URL is the file path, so a rename 404s the post.
#
# Usage: scripts/check-images.sh            # staged additions
#        scripts/check-images.sh --all      # size and pixel audit of the tree
#        scripts/check-images.sh --orphans  # the same, plus unreferenced files
# Env:   MAX_BYTES (default 1572864 = 1.5 MiB), MAX_EDGE (default 2000)
#
# Exit: 0 clean, 1 violations, 2 a tool or path is missing.

set -euo pipefail

ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
cd "$ROOT"

MAX_BYTES="${MAX_BYTES:-1572864}"
MAX_EDGE="${MAX_EDGE:-2000}"

if ! command -v magick >/dev/null 2>&1; then
	echo "error: ImageMagick (magick) not found" >&2
	exit 2
fi

mode="staged"
case "${1:-}" in
	"") ;;
	--all) mode="all" ;;
	--orphans) mode="all"; WANT_ORPHANS=1 ;;
	*) echo "usage: $0 [--all|--orphans]" >&2; exit 2 ;;
esac

exts='\.(png|jpg|jpeg|webp|gif)$'

if [ "$mode" = "staged" ]; then
	mapfile -t files < <(git diff --cached --name-only --diff-filter=A | grep -Ei "$exts" || true)
	if [ "${#files[@]}" -eq 0 ]; then
		echo "no image additions staged; nothing to check"
		exit 0
	fi
else
	mapfile -t files < <(git ls-files | grep -Ei "^imgs/.*$exts" | sort)
fi

fail=0
for f in "${files[@]}"; do
	[ -f "$f" ] || continue
	bytes="$(stat -c%s "$f")"
	read -r w h <<< "$(magick identify -format '%w %h' "$f" 2>/dev/null || echo '0 0')"
	[ "$w" -gt "$h" ] 2>/dev/null && long="$w" || long="$h"
	printf '%8.2f MB  %5dx%-5d  %s\n' \
		"$(awk -v b="$bytes" 'BEGIN{print b/1048576}')" "$w" "$h" "$f"
	if [ "$bytes" -gt "$MAX_BYTES" ] || [ "$long" -gt "$MAX_EDGE" ]; then
		printf '  ^ over limit: %s%s\n' \
			"$([ "$bytes" -gt "$MAX_BYTES" ] && echo "size > $((MAX_BYTES / 1024)) KiB ")" \
			"$([ "$long" -gt "$MAX_EDGE" ] && echo "long edge > ${MAX_EDGE}px")"
		fail=1
	fi
done

if [ "$mode" = "all" ] && [ "${WANT_ORPHANS:-0}" = "1" ]; then
	refs="$(mktemp)"
	trap 'rm -f "$refs"' EXIT
	git ls-files '*.md' '*.yaml' '*.yml' '*.json' '*.py' '*.sh' '*.html' |
		grep -v '^imgs/' |
		xargs -r grep -hoE '[A-Za-z0-9_.-]+\.(png|jpg|jpeg|webp|gif)' 2>/dev/null |
		sort -u > "$refs" || true

	orphans=0
	for f in "${files[@]}"; do
		base="$(basename "$f")"
		# Social derivatives (banners, 1500x600, 5x2 crops) are posted to X and
		# never referenced from a document, so they are not orphans.
		case "$base" in
			*-banner*|*-1500x600*|*-5x2*) continue ;;
		esac
		grep -qx "$base" "$refs" || {
			printf 'orphan: %s\n' "$f"
			orphans=$((orphans + 1))
		}
	done
	[ "$orphans" -gt 0 ] && echo "$orphans image(s) referenced by no tracked text file"
fi

if [ "$fail" -ne 0 ]; then
	echo
	echo "Fix: photograph -> JPEG q85; flat art, table or UI -> PNG with -strip -colors 64."
	echo "     Never rename a published image: Medium's URL is the file path."
	exit 1
fi
echo "all images within limits"
exit 0
