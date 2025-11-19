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
import os
import sys
import shutil
import importlib
import json
import subprocess
import getpass
import platform
from time import time
from datetime import datetime
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# ruamel.yaml YAML factory
from ruamel.yaml import YAML

yaml = YAML(typ="safe")

from fgi.args import parse
from fgi.search import SearchDatabase
from fgi.tagmgr import TagManager
from fgi.media import MediaFactory
from fgi.icon import IconFactory
from fgi.seo.sitemap import Sitemap, SitemapGenerator
from fgi.plugin import PluginManager

from fgi.game import Game
from fgi.author import Author

from fgi.base import sorted_games_name, list_pymod, local_res_src, make_wrapper
from fgi.i18n import get_languages_list, uil10n_load_base, uil10n_load_language
from fgi.stylesheet import make_stylesheet

# NOTE: distutils was removed from the stdlib in Python 3.12.
# Replace usage of distutils.dir_util.copy_tree with a small helper that
# uses shutil.copytree / shutil.copy2 to preserve behavior while keeping
# the exposed interfaces unchanged.
# from distutils import dir_util

# For package version reporting use importlib.metadata (py3.8+)
try:
    import importlib.metadata as importlib_metadata
except Exception:
    import importlib_metadata  # type: ignore


def run_cmd(cmd, failback=""):
    try:
        return subprocess.check_output(cmd).decode("utf-8").rstrip()
    except Exception:
        return failback


def _copy_tree(src, dst):
    """
    Minimal replacement for distutils.dir_util.copy_tree.

    Copies contents of src into dst. If dst doesn't exist it will be created.
    Existing files will be overwritten.
    """
    src = os.fspath(src)
    dst = os.fspath(dst)
    if not os.path.exists(src):
        raise FileNotFoundError(src)
    os.makedirs(dst, exist_ok=True)
    for root, dirs, files in os.walk(src):
        rel = os.path.relpath(root, src)
        target_root = os.path.join(dst, rel) if rel != os.curdir else dst
        os.makedirs(target_root, exist_ok=True)
        for d in dirs:
            os.makedirs(os.path.join(target_root, d), exist_ok=True)
        for f in files:
            sfile = os.path.join(root, f)
            tfile = os.path.join(target_root, f)
            # copy2 preserves metadata similar to distutils.copy_tree
            shutil.copy2(sfile, tfile)


def _safe_version(package_name):
    try:
        return importlib_metadata.version(package_name)
    except Exception:
        return "unknown"


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

        self.tagdep_file = os.path.join(
            self.args.data_dir_prefix, "tag-dependencies.yaml"
        )
        self.tags_file = os.path.join(self.args.data_dir_prefix, "tags.yaml")

        self.dir_templates = [os.path.join(self.args.data_dir_prefix, "templates")]
        self.dir_uil10n = os.path.join(self.args.data_dir_prefix, "uil10n")

        self.webroot_path = [os.path.join(self.args.data_dir_prefix, "webroot", "base")]
        self.styles_path = [
            os.path.join(self.args.data_dir_prefix, "webroot", "styles")
        ]
        self.assets_path = os.path.join(self.args.data_dir_prefix, "assets")
        self.icon_path = os.path.join(self.args.data_dir_prefix, "icons", "build")

        self.dir_doc = os.path.join(self.args.data_dir_prefix, "doc")

        self.base_uri = "https://furrygames.top/"
        self.base_uri_old = "https://furrygamesindex.github.io/"

        self.stylesheets = dict()
        self.author_game_map = dict()

        self.btime_data = None

    def load_game(self, f):
        game = None
        fn = os.path.join(self.dbdir, f)

        if (not os.path.isfile(fn)) or (f[0] == "."):
            return None

        game_id = os.path.splitext(f)[0]

        print("Loading %s" % fn)
        with open(fn) as stream:
            game = Game(yaml.load(stream), game_id, os.path.getmtime(fn))

        for language in self.languages:
            l10n_file = os.path.join(self.dbdir, "l10n", language, f)
            if os.path.isfile(l10n_file):
                print("Loading %s" % l10n_file)
                with open(l10n_file) as stream:
                    game.add_l10n_data(
                        language, yaml.load(stream), os.path.getmtime(l10n_file)
                    )

        return game

    def load_game_all(self):
        games = {}

        for f in sorted_games_name(os.listdir(self.dbdir)):
            game = self.load_game(f)

            if game:
                self.pmgr.invoke_plugins("loader_pre_game_realize", self, game)

                game.realize(
                    self.tagmgr, self.mfac, self.ifac, self.authors, self.btime_data
                )
                games[game.id] = game

                for i in game.authors:
                    if not i.standalone:
                        if i.name not in self.author_game_map:
                            self.author_game_map[i.name] = list()
                        self.author_game_map[i.name].append(game)

                self.sdb.update(game)

        for _, game in games.items():
            game.link(games)

        return games

    def load_author(self, f):
        fn = os.path.join(self.dbdir_author, f)

        if (not os.path.isfile(fn)) or (f[0] == "."):
            return None

        author_id = os.path.splitext(f)[0]

        print("Loading %s" % fn)
        with open(fn) as stream:
            author = Author(yaml.load(stream), author_id)

        return author

    def load_author_all(self):
        authors = dict()

        for f in os.listdir(self.dbdir_author):
            author = self.load_author(f)

            if author:
                author.realize(self.mfac, self.ifac, self.author_game_map)
                authors[author.name] = author

        return authors

    def prepare_tags(self):
        print("Preparing tags")
        print(
            "[note] tag-dependencies.yaml is deprecated and will be removed in future. use implication instead."
        )
        with open(self.tagdep_file) as f:
            self.tagmgr.loaddep(yaml.load(f))
        with open(self.tags_file) as f:
            self.tagmgr.load(yaml.load(f))

    def prepare(self):
        if self.args.plugin:
            for i in self.args.plugin:
                d = i.split(",", 1)
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

        self.sdb = SearchDatabase(self, no_data=self.args.no_searchdb)
        self.sdb.add_extra_data("tagalias", self.tagmgr.tagalias)
        self.sdb.add_extra_data("tagns", self.tagmgr.tagns)

        self.languages = get_languages_list(self, self.dbdir)

        self.env = Environment(loader=FileSystemLoader(self.dir_templates))
        self.env.trim_blocks = True
        self.env.lstrip_blocks = True

        for i in reversed(self.styles_path):
            self.stylesheets.update(make_stylesheet(i))

        if self.output != "-":
            if os.path.exists(self.output) and not self.args.no_purge_prev_builds:
                shutil.rmtree(self.output)
            # reset any previously tracked path state (kept for compatibility with old behavior)
            # create/copy webroot base into output
            for i in reversed(self.webroot_path):
                _copy_tree(i, self.output)

            styles_dirname = os.path.join(self.output, "styles")
            os.makedirs(styles_dirname, exist_ok=True)
            for _, ss in self.stylesheets.items():
                ss.write_to_file(styles_dirname)

            _copy_tree(self.assets_path, os.path.join(self.output, "assets"))
            _copy_tree(self.icon_path, os.path.join(self.output, "icons"))

        if self.args.btime_file:
            with open(self.args.btime_file) as f:
                self.btime_data = json.load(f)

        self.authors = self.load_author_all()
        self.games = self.load_game_all()

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

            Path(os.path.join(self.output, language, "games")).mkdir(
                parents=True, exist_ok=True
            )

            lctx = self.lctx.copy()
            lctx["lang"] = language
            lctx["ui"] = ui

            for f in self.renderer_files:
                print("Rendering %s %s" % (language, f))
                renderer_module = importlib.import_module(
                    ".renderers." + f, package=__package__
                )
                renderer = renderer_module.impl(self, lctx)
                renderer.render()

        lctx = self.lctx.copy()
        lctx["ui"] = self.base_l10n
        for f in self.renderer_nonl10n_files:
            print(f"Rendering nonl10n {f}")
            renderer_module = importlib.import_module(
                ".renderers.nonl10n." + f, package=__package__
            )
            renderer = renderer_module.impl(self, lctx)
            renderer.render()

        self.sitemap.save(self.output)

        buildinfo_path = os.path.join(self.args.output, "_buildinfo.txt")
        with open(buildinfo_path, "w") as f:
            f.write("# FGI BUILD INFO START\n")
            f.write(
                f"base revision: {run_cmd(['git', 'rev-parse', 'HEAD'], failback='unknown')}\n"
            )
            f.write(f"options: {' '.join(self.argv[:-1])}\n")
            f.write(f"build datetime: {datetime.utcnow()}\n")
            f.write(f"builder: {getpass.getuser()}@{platform.uname()[1]}\n")
            f.write("interpreter: ")
            f.write(sys.version.replace("\n", " "))
            f.write("\n")
            # Use importlib.metadata for package versions in a python-3.12-safe way
            f.write(f"jinja2 version: {_safe_version('jinja2')}\n")
            # ruamel.yaml package distribution name can vary; try typical names
            ruamel_pkg = _safe_version("ruamel.yaml") or _safe_version(
                "ruamel.yaml.clib"
            )
            f.write(f"ruamel.yaml version: {ruamel_pkg}\n")
            f.write(f"markdown2 version: {_safe_version('markdown2')}\n")
            f.write(f"BeautifulSoup version: {_safe_version('beautifulsoup4')}\n")
            f.write(
                f"webp utils version: {run_cmd(['cwebp', '-version'], failback='unknown')}\n"
            )
            f.write("# ADDITIONAL PATCHES\n")
            if os.path.exists(".patches_info"):
                with open(".patches_info") as pi:
                    f.write(pi.read())

            f.write("# PLUGINS INFOMATION\n")
            # keep plugin callback but be defensive: plugins may expect file-like or path
            try:
                self.pmgr.invoke_plugins("post_build", f, self.output)
            except TypeError:
                # fallback: pass output path only
                try:
                    self.pmgr.invoke_plugins("post_build", self.output)
                except Exception:
                    pass
            except Exception:
                pass

            f.write("# FGI BUILD INFO END\n")


def main(argv):
    gen = Generator(argv[1:])
    gen.prepare()
    gen.run()
