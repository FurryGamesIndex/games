#!/usr/bin/env bash

set -e

game_deprecated_properties=(
	"tags.author" 
	"sensitive_media" 
)

function info() {
	echo "[lint] $@"
}

function die() {
	echo "[lint] $@" >&2
	exit 255
}

function on_error() {
	die "check failed"
}
trap on_error ERR

case "$1" in
game)
	gid=$(basename "$2" | cut -d / -f 2 | cut -d . -f 1)
	info "checking game '$gid' ..."

	if [ "$LINT_OLD_FILES_EXEMPTION" = "true" ]; then
		mtime=$(stat -c %Y "$2")
		if test "$mtime" -lt 1628425073; then
			info "game exempted"
			exit 0
		fi
	fi

	./scripts/validate.py schemas/game.schema.yaml "$2"
	info "schema check pass"

	# ./scripts/imageutils.sh validate-thumbnail $(echo -n "assets/${gid}/"; ./scripts/dbutils.sh game-get-property "$gid" thumbnail)
	# info "thumbnail chack pass"

	for i in "${game_deprecated_properties[@]}"; do
		./scripts/dbutils.sh game-has-property "$gid" "$i" && die "Deprecated property '$i' should not be used in new entries."
	done
	info "deprecated properties check pass"

	info "all check done without errors"
	;;
game-l10n)
	info "checking game-l10n '$2' ..."

	./scripts/validate.py schemas/game-l10n.schema.yaml "$2"
	info "schema check pass"

	info "all check done without errors"
	;;
esac
