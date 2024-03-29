#!/usr/bin/env bash

function err() {
	echo $* >&2
	exit 1
}

function name2id() {
	echo $* | sed -E -e 's/ /_/g' -e 's/_{2,}/_/g' -e 's/_+$//g'
}

function readx() {
	declare -n _readx="$2"
	read -rp "$1" _readx
	[ -z "$_readx" ] && _readx="$3"
}

function yaml2json() {
	python3 - "$1" <<EOF
import yaml
import json
import sys

with open(sys.argv[1]) as f:
    print(json.dumps(yaml.safe_load(f)))
EOF
}

case "$1" in
new-author)
	readx "What's the name of the author: " name
	id=$(name2id $name)
	readx "What's the ID of the author [$id]: " id $id

	[ -f "authors/$id.yaml" ] && err "File already exist: authors/$id.yaml"

	avatar=$id.jpg
	readx "What's the avatar file name of the author [$avatar]: " avatar $avatar
	type=""

	echo "Select the type of the author: "
	select x in $(yaml2json schemas/author.schema.yaml | jq -r '.properties.type.enum | join(" ")') ; do
		typename=$x
		break
	done

	tee "authors/$id.yaml" <<EOF
# Generated by dbutils.sh
# remove these comment after you acknowledged/edited it

name: $name

type: $typename

avatar: $avatar

#, fuzzy
links:
  - name: STUB
    uri: /_stub
EOF
	;;
new-game)
	readx "What's the name of the game: " name
	id=$(name2id $name)
	readx "What's the ID of the game [$id]: " id $id

	[ -f "games/$id.yaml" ] && err "File already exist: games/$id.yaml"

	thumbnail=$id.jpg
	readx "What's the thumbnail file name of the game [$thumbnail]: " thumbnail $thumbnail

	echo "Select the format of the description: "
	select x in plain markdown ; do
		descfmt=$x
		break
	done

	desc=''
	echo "Input the description, end with '.' or EOF"
	while read -r line ; do
		[ "$line" = . ] && break
		desc="$desc"$'\n'"$line"
	done

	desc="$(sed 's/^/  /g' <<< "$desc")"
	[ $descfmt != plain ] && desc="$desc"$'\n\n'"description-format: $descfmt"

	tee "games/$id.yaml" <<EOF
# Generated by dbutils.sh
# remove these comment after you acknowledged/edited it

name: $name

description: |
$desc

#, fuzzy
authors:

#, fuzzy
tags:

#, fuzzy
links:

thumbnail: $thumbnail

#, fuzzy
screenshots:
EOF
	;;
show-tagdep)
	python3 - <<EOF
from fgi.generate import Generator

gen = Generator(["-"])
gen.prepare_tags()
for ns, v in gen.tagmgr.tagdep.items():
    for tag, dep in v.items():
        ftag = ns + ":" + tag
        print(f"{ftag:>26}  implicate  {dep}")
EOF
	;;
list-games)
	cd games
	ls *.yaml | cut -d . -f 1
	;;
list-game-files)
	ls games/*.yaml
	;;
list-game-l10n-files)
	ls games/l10n/*/*.yaml
	;;
game-get-property)
	yaml2json "games/$2.yaml" | jq -r ".$3"
	;;
game-has-property)
	yaml2json "games/$2.yaml" | jq -r -e ".$3" > /dev/null 2>&1
	;;
*)
	echo Unknown command $1
	exit 1
	;;
esac
