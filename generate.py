#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 
# Copyright (C) 2020 Utopic Panther
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# 

import yaml
import os
import shutil
import importlib
from sys import argv
import json
from pathlib import Path
from distutils import dir_util
from jinja2 import Environment, FileSystemLoader

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--extra-ui', type=str, help='Set extra ui profile path')
parser.add_argument('--no-sitemap', default=False, action='store_true', help='Do not generate sitemap')
parser.add_argument('--no-searchdb', default=False, action='store_true', help='Do not generate searchdb')
parser.add_argument('--no-purge-prev-builds', default=False, action='store_true', help='Do not purge previous builds')
parser.add_argument('--download-external-images', default=False, action='store_true', help='Download external images to output dir')
parser.add_argument('--use-external-images-cache', type=str, help='Set a previous builds dir to avoid to download repeatly')
parser.add_argument('output', type=str, help='Output path')

args = parser.parse_args()

from utils.search import searchdb
from utils import tagmgr
from utils.seo import sitemap
from utils.seo import keywords


dir = "games"
output = args.output
sitemap.ignore = args.no_sitemap

renderer_files = [os.path.splitext(f)[0] \
        for f in os.listdir("renderers") \
        if os.path.isfile(os.path.join("renderers", f)) and f[0] != '.']
languages = [f for f in os.listdir(os.path.join(dir, "l10n"))]
games = {}

with open("tag-dependencies.yaml") as f:
    tagmgr.loaddep(yaml.safe_load(f))
with open("tags.yaml") as f:
    tagmgr.load(yaml.safe_load(f))

sdb = searchdb(stub = args.no_searchdb)

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

    tagmgr.check_and_patch(games[game_id])
    sdb.update(games[game_id])

env = Environment(loader = FileSystemLoader("templates"))

if os.path.exists(output) and not args.no_purge_prev_builds:
    shutil.rmtree(output)
#shutil.copytree("webroot", output)
#shutil.copytree("assets", os.path.join(output, "assets"))
dir_util.copy_tree("webroot", output)
dir_util.copy_tree("assets", os.path.join(output, "assets"))

if not args.no_searchdb:
    with open(os.path.join(output, "scripts", "searchdb.json"), "w") as f:
        f.write(json.dumps(sdb.db))

languages.append('en')
with open(os.path.join("uil10n", "en.yaml")) as stream:
    base_l10n = yaml.safe_load(stream)
if args.extra_ui is not None:
    with open(os.path.join(args.extra_ui, "en.yaml")) as stream:
        base_l10n.update(yaml.safe_load(stream))

print("Rendering misc single pages")
renderer = importlib.import_module("utils.singles-misc-renderer")
renderer.render(games, env, "c", base_l10n, output)

for language in languages:
    with open(os.path.join("uil10n", language + ".yaml")) as stream:
        ui = base_l10n.copy()
        ui.update(yaml.safe_load(stream))
        keywords.preprocess_keywords(ui)
    if args.extra_ui is not None:
        euifn = os.path.join(args.extra_ui, language + ".yaml") 
        if os.path.isfile(euifn):
            with open(euifn) as stream:
                ui.update(yaml.safe_load(stream))
    
    Path(os.path.join(output, language, "games")).mkdir(parents=True, exist_ok=True)

    for f in renderer_files:
        print("Rendering %s %s" % (language, f))
        renderer = importlib.import_module("renderers." + f)
        renderer.render(games, env, language, ui, output)

sitemap.write_to_file(os.path.join(output, "sitemap.xml"))
