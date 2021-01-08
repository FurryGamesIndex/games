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
from fgi.base import load_game_all, list_pymod, local_res_href, make_wrapper
from fgi.search import SearchDatabase
from fgi.tagmgr import TagManager
from fgi.media import MediaFactory
from fgi.seo import sitemap
from fgi.i18n import get_languages_list, uil10n_load_base, uil10n_load_language
from fgi.plugin import PluginManager

def run_cmd(cmd, failback=''):
    try:
        return subprocess.check_output(cmd).decode('utf-8').rstrip()
    except:
        return failback

class Generator:
    def __init__(self, args):
        self.args = args

        self.dbdir = "games"
        self.output = self.args.output

        self.dir_renderer_files = "renderers"
        self.dir_renderer_nonl10n_files = os.path.join("renderers", "nonl10n")

        self.pmgr = PluginManager()
        self.tagmgr = TagManager()
        self.mfac = MediaFactory(self)

        self.tagdep_file = "tag-dependencies.yaml"
        self.tags_file = "tags.yaml"

        self.dir_templates = "templates"
        self.dir_uil10n = "uil10n"

        self.webroot_path = "webroot"
        self.assets_path = "assets"

    def prepare(self):
        if self.args.plugin:
            for i in self.args.plugin:
                d = i.split(',', 1)
                name = d[0]
                options = None
                if len(d) >= 2:
                    options = d[1]
                self.pmgr.load_plugin(name, options)

        self.renderer_files = list_pymod(self.dir_renderer_files)
        self.renderer_nonl10n_files = list_pymod(self.dir_renderer_nonl10n_files)

        with open(self.tagdep_file) as f:
            self.tagmgr.loaddep(yaml.safe_load(f))
        with open(self.tags_file) as f:
            self.tagmgr.load(yaml.safe_load(f))

        self.sdb = SearchDatabase(self, no_data = self.args.no_searchdb)
        self.sdb.add_extra_data("tagalias", self.tagmgr.tagalias)
        self.sdb.add_extra_data("tagns", self.tagmgr.tagns)

        self.languages = get_languages_list(self, self.dbdir)

        self.env = Environment(loader = FileSystemLoader(self.dir_templates))

        if self.output != "-":
            if os.path.exists(self.output) and not self.args.no_purge_prev_builds:
                shutil.rmtree(self.output)
            dir_util._path_created = {}
            dir_util.copy_tree(self.webroot_path, self.output)
            dir_util.copy_tree(self.assets_path, os.path.join(self.output, "assets"))

        self.games = load_game_all(self.dbdir, self.sdb, self.tagmgr, self.languages, self.mfac)

        self.base_l10n = uil10n_load_base(self, self.dir_uil10n)

        self.lctx = {
            "os": os,
            "time": time,
            "res": make_wrapper(local_res_href, self.pmgr),
            "args": self.args,
            "games": self.games,
            "webrootdir": self.webroot_path,
        }

    def run(self):
        self.sdb.write_to_file(self.output)

        for language in self.languages:
            ui = uil10n_load_language(self, self.dir_uil10n, self.base_l10n, language)
            
            Path(os.path.join(self.output, language, "games")).mkdir(parents=True, exist_ok=True)

            lctx = self.lctx.copy()
            lctx["lang"] = language
            lctx["ui"] = ui

            for f in self.renderer_files:
                print("Rendering %s %s" % (language, f))
                renderer_module = importlib.import_module(".renderers." + f, package=__package__)
                renderer = renderer_module.impl(self, lctx)
                renderer.render()

        lctx = self.lctx.copy()
        lctx["ui"] = self.base_l10n
        for f in self.renderer_nonl10n_files:
            print(f"Rendering nonl10n {f}")
            renderer_module = importlib.import_module(".renderers.nonl10n." + f, package=__package__)
            renderer = renderer_module.impl(self, lctx)
            renderer.render()

        sitemap.write_to_file(self.output)

        self.pmgr.invoke_plugins("post_build", None, output_path = self.output)

def main(argv):
    argv = argv[1:]

    # FIXME: --start--
    # These global stuffs should be refector to Generator object context
    args = parse(argv)

    sitemap.ignore = args.no_sitemap
    # FIXME: --end--

    gen = Generator(args)
    gen.prepare()
    gen.run()

    with open(os.path.join(args.output, "_buildinfo.txt"), "w") as f:
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
