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
import yaml
from markdown2 import Markdown

from fgi.seo import keywords
from fgi.plugin import invoke_plugins


def get_languages_list(dbdir, args):
    ll = [f for f in os.listdir(os.path.join(dbdir, "l10n"))]
    ll.append("en")

    # FIXME: uncompleted languages is blacklisted
    if not args.next:
        ll.remove("ja")

    ll = invoke_plugins("i18n_post_ll_done", ll)

    return ll

def uil10n_load_base(l10ndir, args):
    base_l10n = None

    with open(os.path.join(l10ndir, "en.yaml")) as stream:
        base_l10n = yaml.safe_load(stream)
        keywords.preprocess_keywords(base_l10n)

    if args.extra_ui is not None:
        with open(os.path.join(args.extra_ui, "en.yaml")) as stream:
            base_l10n.update(yaml.safe_load(stream))

    base_l10n = invoke_plugins("i18n_post_load_uil10n_base_data", base_l10n)

    return base_l10n

def ui10n_load_language(l10ndir, base_l10n, language, args):
    ui = None

    with open(os.path.join(l10ndir, language + ".yaml")) as stream:
        ui = base_l10n.copy()
        ui.update(yaml.safe_load(stream))
        keywords.preprocess_keywords(ui)

    puifn = os.path.join(l10ndir, language + "_PRIVATE.yaml") 
    if os.path.isfile(puifn):
        with open(puifn) as stream:
            ui.update(yaml.safe_load(stream))

    if args.extra_ui is not None:
        euifn = os.path.join(args.extra_ui, language + ".yaml")
        if os.path.isfile(euifn):
            with open(euifn) as stream:
                ui.update(yaml.safe_load(stream))

    ui = invoke_plugins("i18n_post_load_uil10n_language_data", ui, language=language, base_l10n=base_l10n)

    return ui


def get(game, language, key):
    l10n_value = game["tr"].get(language, {}).get(key)
    if l10n_value is not None:
        return l10n_value
    else:
        return game[key]

doc_markdowner = Markdown(extras=["tables", "metadata"])
doc_md_cache = dict()

def _conv_doc_markdown_get_content(fn, callback):
    with open(fn) as f:
        content = f.read()
        if callback is not None:
            content = callback(content)
        return content

def conv_doc_markdown(name, language, callback=None):
    if language is None:
        content = _conv_doc_markdown_get_content(f"doc/{name}.md", callback)
        result = doc_markdowner.convert(content)
    else:
        fn = f"doc/{name}.{language}.md"
        fnen = f"doc/{name}.en.md"
        if name not in doc_md_cache:
            content = _conv_doc_markdown_get_content(fnen, callback)
            doc_md_cache[name] = doc_markdowner.convert(content)

        if language == "en" or not os.path.exists(fn):
            return doc_md_cache[name]

        content = _conv_doc_markdown_get_content(fn, callback)

        result = doc_markdowner.convert(content)
        if doc_md_cache[name].metadata:
            result.metadata = { **doc_md_cache[name].metadata, **result.metadata }

    return result
