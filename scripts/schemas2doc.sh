#!/usr/bin/env bash

set -e

yaml2json() {
	python3 - "$1" <<EOF
import yaml
import json
import sys

with open(sys.argv[1]) as f:
    print(json.dumps(yaml.safe_load(f)))
EOF
}

TEMP=$(mktemp -d /tmp/FGI.XXXXXX)

mkdir "$TEMP/schemas"

for i in schemas/*.schema.yaml; do
	name=$(basename $i)
	name="${name%.yaml}.json"
	yaml2json "$i" > "$TEMP/schemas/$name"
done

rm -rf "doc/spec"

# https://github.com/adobe/jsonschema2md
# npm install -g @adobe/jsonschema2md
jsonschema2md -d "$TEMP/schemas/" -n -h false -o "doc/spec/" -x "$TEMP/hole"

rm -rf "$TEMP"
