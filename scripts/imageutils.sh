#!/usr/bin/env bash

set -e

function err() {
	echo "$@"
	exit 1
}

function image_size_validate_small() {
	w=$(identify -format '%w' "$1")
	h=$(identify -format '%h' "$1")

	[ "$w" -gt "360" ] && return 1
	[ "$h" -gt "168" ] && return 1

	lp=$(bc <<< "168*$w")
	rp=$(bc <<< "360*$h")

	[ "$lp" = "$rp" ] || return 2

	return 0
}

case "$1" in
compress-avatar)
	convert -strip -resize 64x64 -quality 75 "$2" "$3"
	;;
validate-thumbnail)
	shift
	set +e

	echo -n "$1:"
	r=$(identify -format '%wx%h' "$1")
	[ "$?" = "0" ] || err "ImageMagick error"

	[ "$r" = "360x168" ] || image_size_validate_small "$1" || err "Wrong size: $r ($?)"

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
