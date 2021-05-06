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
from fgi.search import SearchDatabase
from fgi.tagmgr import TagManager
from fgi.media import MediaFactory
from fgi.icon import IconFactory
from fgi.seo.sitemap import Sitemap, SitemapGenerator
from fgi.plugin import PluginManager

from fgi.base import load_game_all, load_author_all, list_pymod, local_res_src, make_wrapper
from fgi.i18n import get_languages_list, uil10n_load_base, uil10n_load_language
from fgi.stylesheet import make_stylesheet

def run_cmd(cmd, failback=''):
    try:
        return subprocess.check_output(cmd).decode('utf-8').rstrip()
    except:
        return failback

class Generator:
    def __init__(self, argv):
        self.argv = argv
        self.args = parse(argv)

        self.dbdir = os.path.join(self.args.data_dir_prefix, "games")
        self.dbdir_author = os.path.join(self.args.data_dir_prefix, "authors")
        self.output = self.args.output

        self.dir_renderer_files = "renderers"
        self.dir_renderer_nonl10n_files = os.path.join("renderers", "nonl10n")

        self.pmgr = PluginManager()
        self.tagmgr = TagManager()
        self.mfac = MediaFactory(self)

        self.tagdep_file = os.path.join(self.args.data_dir_prefix, "tag-dependencies.yaml")
        self.tags_file = os.path.join(self.args.data_dir_prefix, "tags.yaml")

        self.dir_templates = [ os.path.join(self.args.data_dir_prefix, "templates") ]
        self.dir_uil10n = os.path.join(self.args.data_dir_prefix, "uil10n")

        self.webroot_path = [ os.path.join(self.args.data_dir_prefix, "webroot", "base") ]
        self.styles_path = [ os.path.join(self.args.data_dir_prefix, "webroot", "styles") ]
        self.assets_path = os.path.join(self.args.data_dir_prefix, "assets")
        self.icon_path = os.path.join(self.args.data_dir_prefix, "icons", "build")

        self.dir_doc = os.path.join(self.args.data_dir_prefix, "doc")

        self.base_uri = "https://furrygames.top/"
        self.base_uri_old = "https://furrygamesindex.github.io/"

        self.stylesheets = dict()
        self.author_game_map = dict()

    def prepare_tags(self):
        print("Preparing tags")
        print("[note] tag-dependencies.yaml is deprecated and will be removed in future. use implication instead.")
        with open(self.tagdep_file) as f:
            self.tagmgr.loaddep(yaml.safe_load(f))
        with open(self.tags_file) as f:
            self.tagmgr.load(yaml.safe_load(f))

    def prepare(self):
        if self.args.plugin:
            for i in self.args.plugin:
                d = i.split(',', 1)
                name = d[0]
                options = None
                if len(d) >= 2:
                    options = d[1]
                self.pmgr.load_plugin(name, options)

        self.pmgr.invoke_plugins("global_pre_initialization", self)

        with open(os.path.join(self.icon_path, "FGI-icons.json")) as f:
            icondata = json.load(f)
        self.ifac = IconFactory(icondata)

        self.sitemap = SitemapGenerator()
        if not self.args.no_sitemap:
            self.sitemap.add_site(Sitemap(self.base_uri, "sitemap2.xml"))
            self.sitemap.add_site(Sitemap(self.base_uri_old, "sitemap.xml"))

        self.renderer_files = list_pymod(self.dir_renderer_files)
        self.renderer_nonl10n_files = list_pymod(self.dir_renderer_nonl10n_files)

        self.prepare_tags()

        self.sdb = SearchDatabase(self, no_data = self.args.no_searchdb)
        self.sdb.add_extra_data("tagalias", self.tagmgr.tagalias)
        self.sdb.add_extra_data("tagns", self.tagmgr.tagns)

        self.languages = get_languages_list(self, self.dbdir)

        self.env = Environment(loader = FileSystemLoader(self.dir_templates))
        self.env.trim_blocks = True
        self.env.lstrip_blocks = True

        for i in reversed(self.styles_path):
            self.stylesheets.update(make_stylesheet(i))

        if self.output != "-":
            if os.path.exists(self.output) and not self.args.no_purge_prev_builds:
                shutil.rmtree(self.output)
            dir_util._path_created = {}
            for i in reversed(self.webroot_path):
                dir_util.copy_tree(i, self.output)

            styles_dirname = os.path.join(self.output, "styles")
            os.mkdir(styles_dirname)
            for _, ss in self.stylesheets.items():
                ss.write_to_file(styles_dirname)

            dir_util.copy_tree(self.assets_path, os.path.join(self.output, "assets"))
            dir_util.copy_tree(self.icon_path, os.path.join(self.output, "icons"))

        self.authors = load_author_all(self.dbdir_author, self.mfac, self.ifac, self.author_game_map)
        self.games = load_game_all(self.dbdir, self.sdb, self.tagmgr, self.languages, self.mfac, self.ifac, self.authors, self.author_game_map)

        self.base_l10n = uil10n_load_base(self, self.dir_uil10n)

        self.lctx = {
            "os": os,
            "time": time,
            "res": make_wrapper(local_res_src, self),
            "args": self.args,
            "games": self.games,
            "authors": self.authors,
            "author_game_map": self.author_game_map,
            "ifac": self.ifac,
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

        self.sitemap.save(self.output)

        with open(os.path.join(self.args.output, "_buildinfo.txt"), "w") as f:
            f.write("# FGI BUILD INFO START\n")
            f.write(f"base revision: {run_cmd(['git', 'rev-parse', 'HEAD'], failback='unknown')}\n")
            f.write(f"options: {' '.join(self.argv[:-1])}\n")
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

        self.pmgr.invoke_plugins("post_build", None, output_path = self.output)

def main(argv):
    gen = Generator(argv[1:])
    gen.prepare()
    gen.run()
