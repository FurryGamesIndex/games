#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
import os
import shutil
import importlib
from sys import argv
import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

from utils.search import searchdb

dir = "games"
if len(argv) < 2:
    output = "output"
else:
    output = argv[1]

renderer_files = [os.path.splitext(f)[0] \
        for f in os.listdir("renderers") \
        if os.path.isfile(os.path.join("renderers", f)) and f[0] != '.']
languages = [f for f in os.listdir(os.path.join(dir, "l10n"))]
games = {}

sdb = searchdb()

for f in sorted(os.listdir(dir)):
    file = os.path.join(dir, f)
    game_id = os.path.splitext(f)[0]

    if (not os.path.isfile(file)) or (f[0] == '.'):
        continue

    print("Loading %s" % file)
    with open(file) as stream:
        games[game_id] = yaml.safe_load(stream)
        games[game_id]["id"] = game_id
        games[game_id]["tr"] = {}

    for language in languages:
        l10n_file = os.path.join(dir, "l10n", language, f)
        if os.path.isfile(l10n_file):
            print("Loading %s" % l10n_file)
            with open(l10n_file) as stream:
                games[game_id]["tr"][language] = yaml.safe_load(stream)

    sdb.update(games[game_id])

env = Environment(loader = FileSystemLoader("templates"))

if os.path.exists(output):
    shutil.rmtree(output)
shutil.copytree("webroot", output)
shutil.copytree("assets", os.path.join(output, "assets"))

with open(os.path.join(output, "scripts", "searchdb.json"), "w") as f:
    f.write(json.dumps(sdb.db))

languages.append('en')
with open(os.path.join("uil10n", "en.yaml")) as stream:
    base_l10n = yaml.safe_load(stream)

print("Rendering misc single pages")
renderer = importlib.import_module("utils.singles-misc-renderer")
renderer.render(games, env, "c", base_l10n, output)

for language in languages:
    with open(os.path.join("uil10n", language + ".yaml")) as stream:
        ui = base_l10n.copy()
        ui.update(yaml.safe_load(stream))
    
    output_dir = os.path.join(output, language)

    for f in renderer_files:
        print("Rendering %s %s" % (language, f))
        Path(os.path.join(output_dir, "games")).mkdir(parents=True, exist_ok=True)
        renderer = importlib.import_module("renderers." + f)
        renderer.render(games, env, language, ui, output_dir)
