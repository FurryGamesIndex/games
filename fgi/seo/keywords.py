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

def preprocess_keywords(ui):
    kwds = ui["_base_keywords"] + ui["base_keywords"]
    ui["base_keywords"] = ", ".join(kwds)

    for i in [ "gay", "yiff", "vn" ]:
        ui["kwd_" + i] = ui["_kwd_" + i] + ui["kwd_" + i]

def game_page_extra_keywords(game, ui):
    tags = game.tags
    kwds = []
    if "bara" in tags.get("type", {}):
        kwds += ui["kwd_gay"]
    if "yiff" in tags.get("type", {}):
        kwds += ui["kwd_yiff"]
    if "visual-novel" in tags.get("type", {}):
        kwds += ui["kwd_vn"]

    if not kwds:
        return ""
    else:
        return ", " + ", ".join(kwds)
