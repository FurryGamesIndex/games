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
import jinja2
import subprocess
import getpass
import platform
import markdown2
import bs4
from time import time
from datetime import datetime
from pathlib import Path
from distutils import dir_util
from jinja2 import Environment, FileSystemLoader

from fgi.args import parse
from fgi.base import load_game_all, list_pymod
from fgi.search import searchdb
from fgi.tagmgr import TagManager
from fgi.seo import sitemap
from fgi.i18n import get_languages_list, uil10n_load_base, ui10n_load_language
from fgi.plugin import invoke_plugins

def run_cmd(cmd, failback=''):
    try:
        return subprocess.check_output(cmd).decode('utf-8').rstrip()
    except:
        return failback


def local_res_href(rr, path, hc_uquery = None):
    query = ""
    if hc_uquery:
        query = f"?hc=uquery&t={hc_uquery}"

    mod = invoke_plugins("html_local_res_href", None, rr=rr, path=path, hc_uquery=hc_uquery)

    if mod:
        mod_value = mod["new_uri"]
        if "query_mode" in mod:
            if mod["query_mode"] == "unmanaged":
                mod_value = mod_value + query
            elif mod["query_mode"] == "origin-first":
                if query != "":
                    mod_value = mod_value + query
                else:
                    mod_value = mod_value + mod["query_fb"]
            elif mod["query_mode"] == "managed":
                pass
            else:
                raise ValueError(f"unkown query_mode: {mode['query_mode']}")
        return mod_value
    else:
        return rr + path + query

def main(argv):
    argv = argv[1:]
    parse(argv)
    from fgi.args import args

    dbdir = "games"
    output = args.output
    sitemap.ignore = args.no_sitemap

    renderer_files = list_pymod("renderers")
    renderer_nonl10n_files = list_pymod(os.path.join("renderers", "nonl10n"))

    tagmgr = TagManager()

    with open("tag-dependencies.yaml") as f:
        tagmgr.loaddep(yaml.safe_load(f))
    with open("tags.yaml") as f:
        tagmgr.load(yaml.safe_load(f))

    sdb = searchdb(no_data = args.no_searchdb)
    sdb.add_extra_data("tagalias", tagmgr.tagalias)
    sdb.add_extra_data("tagns", tagmgr.tagns)

    if os.path.exists(output) and not args.no_purge_prev_builds:
        shutil.rmtree(output)
    dir_util._path_created = {}
    dir_util.copy_tree("webroot", output)
    dir_util.copy_tree("assets", os.path.join(output, "assets"))

    games = load_game_all(dbdir, sdb, tagmgr)

    env = Environment(loader = FileSystemLoader("templates"))

    sdb.write_to_file(output)

    languages = get_languages_list(dbdir)
    base_l10n = uil10n_load_base("uil10n")

    lctx = {
        "args": args,
        "searchdb": sdb,
        "os": os,
        "webrootdir": "webroot",
        "time": time,
        "res": local_res_href,
    }

    for language in languages:
        ui = ui10n_load_language("uil10n", base_l10n, language)
        
        Path(os.path.join(output, language, "games")).mkdir(parents=True, exist_ok=True)

        lctx["lang"] = language
        lctx["ui"] = ui

        for f in renderer_files:
            print("Rendering %s %s" % (language, f))
            renderer = importlib.import_module(".renderers." + f, package=__package__)
            renderer.render(games, env, lctx, output)

    lctx["ui"] = base_l10n
    for f in renderer_nonl10n_files:
        print(f"Rendering nonl10n {f}")
        renderer = importlib.import_module(".renderers.nonl10n." + f, package=__package__)
        renderer.render(games, env, lctx, output)

    sitemap.write_to_file(output)

    invoke_plugins("post_build", None, output_path = output)

    with open(os.path.join(output, "_buildinfo.txt"), "w") as f:
        f.write("# FGI BUILD INFO START\n")
        f.write(f"base revision: {run_cmd(['git', 'rev-parse', 'HEAD'], failback='unknown')}\n")
        f.write(f"options: {' '.join(argv[:-1])}\n")
        f.write(f"build datetime: {datetime.utcnow()}\n")
        f.write(f"builder: {getpass.getuser()}@{platform.uname()[1]}\n")
        f.write("interpreter: ")
        f.write(sys.version.replace("\n", " "))
        f.write("\n")
        f.write(f"jinja2 version: {jinja2.__version__}\n")
        f.write(f"pyyaml version: {yaml.__version__}\n")
        f.write(f"markdown2 version: {markdown2.__version__}\n")
        f.write(f"BeautifulSoup version: {bs4.__version__}\n")
        f.write(f"webp utils version: {run_cmd(['cwebp', '-version'], failback='unknown')}\n")
        f.write("# ADDITIONAL PATCHES\n")
        if os.path.exists(".patches_info"):
            with open(".patches_info") as pi:
                f.write(pi.read())
        f.write("# FGI BUILD INFO END\n")
