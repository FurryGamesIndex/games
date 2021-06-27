#!/usr/bin/env bash

set -e

function err() {
	echo "$@"
	exit 1
}

case "$1" in
compress-avatar)
	convert -strip -resize 64x64 -quality 75 "$2" "$3"
	;;
validate-thumbnail)
	shift
	echo -n "$1:"
	r=$(identify -format '%wx%h' "$1")

	[ "$r" = "360x168" ] || err "Wrong size: $r"

	echo "OK"
	;;
validate-all-thumbnails)
	./scripts/dbutils.sh list-games |\
		xargs -I{} bash -c 'echo -n assets/{}/ ; ./scripts/dbutils.sh game-get-property {} thumbnail' |\
		xargs -I{} ./scripts/imageutils.sh validate-thumbnail {} 
	;;
*)
	echo Unknown command $1
	exit 1
	;;
esac
