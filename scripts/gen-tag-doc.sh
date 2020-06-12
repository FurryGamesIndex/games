#!/usr/bin/env bash

./scripts/doctag.py en > doc/tags.en.md
./scripts/doctag.py zh-cn > doc/tags.zh-cn.md
./zhconv.py --no-builtin doc/tags.zh-cn.md:doc/tags.zh-tw.md
