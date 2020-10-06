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

from html import escape
from markdown2 import Markdown

from core import image

def get_languages_list(dbdir):
    return [f for f in os.listdir(os.path.join(dbdir, "l10n"))]

def get(game, language, key):
    l10n_value = game["tr"].get(language, {}).get(key)
    if l10n_value is not None:
        return l10n_value
    else:
        return game[key]

def get_desc(rr, game, language):
    desc = get(game, language, "description")
    if "description-format" not in game:
        return escape(desc).replace("\n", "<br>")
    elif game["description-format"] == "markdown":
        markdowner = Markdown(extras=["strike", "target-blank-links"],
                inline_image_uri_filter = lambda uri: image.uri(rr, uri, game["id"]))
        return markdowner.convert(desc)
    else:
        raise ValueError("description format invaild")

