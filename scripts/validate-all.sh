#!/usr/bin/env bash

set -e

for i in games/*; do
	[ -f "$i" ] || continue
	echo "Validating '$i'"
	./scripts/validate.py ./schemas/game.schema.yaml "$i"
done

for i in games/l10n/*/*; do
	[ -f "$i" ] || continue
	echo "Validating '$i'"
	./scripts/validate.py ./schemas/game-l10n.schema.yaml "$i"
done

for i in authors/*; do
	[ -f "$i" ] || continue
	echo "Validating '$i'"
	./scripts/validate.py ./schemas/author.schema.yaml "$i"
done
