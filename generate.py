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
import sys
import shutil
import argparse
import importlib
import json
from pathlib import Path
from distutils import dir_util
from jinja2 import Environment, FileSystemLoader

from core.base import *
from core.args import parse
from core.search import searchdb
from core import tagmgr
from core.seo import sitemap
from core.i18n import get_languages_list, uil10n_load_base, ui10n_load_language

def main(argv):
    parse(argv[1:])
    from core.args import args

    dbdir = "games"
    output = args.output
    sitemap.ignore = args.no_sitemap

    renderer_files = [os.path.splitext(f)[0] \
            for f in os.listdir("renderers") \
            if os.path.isfile(os.path.join("renderers", f)) and f[0] != '.']

    with open("tag-dependencies.yaml") as f:
        tagmgr.loaddep(yaml.safe_load(f))
    with open("tags.yaml") as f:
        tagmgr.load(yaml.safe_load(f))

    sdb = searchdb(stub = args.no_searchdb)

    if os.path.exists(output) and not args.no_purge_prev_builds:
        shutil.rmtree(output)
    dir_util.copy_tree("webroot", output)
    dir_util.copy_tree("assets", os.path.join(output, "assets"))

    games = load_game_all(dbdir, sdb)

    env = Environment(loader = FileSystemLoader("templates"))

    if not args.no_searchdb:
        with open(os.path.join(output, "scripts", "searchdb.json"), "w") as f:
            f.write(json.dumps(sdb.db))

    languages = get_languages_list(dbdir)
    languages.append('en')

    base_l10n = uil10n_load_base("uil10n")

    print("Rendering misc single pages")
    renderer = importlib.import_module("core.singles-misc-renderer")
    renderer.render(games, env, "c", base_l10n, output)

    for language in languages:
        ui = ui10n_load_language("uil10n", base_l10n, language)
        
        Path(os.path.join(output, language, "games")).mkdir(parents=True, exist_ok=True)

        for f in renderer_files:
            print("Rendering %s %s" % (language, f))
            renderer = importlib.import_module("renderers." + f)
            renderer.render(games, env, language, ui, output)

    sitemap.write_to_file(os.path.join(output, "sitemap.xml"))

if __name__ == "__main__":
    main(sys.argv)
