#!/usr/bin/env bash

set -e

case "$1" in
avatar)
	convert -strip -resize 64x64 -quality 75 "$2" "$3"
	;;
esac
