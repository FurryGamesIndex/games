# -*- coding: utf-8 -*-

# 
# Copyright (C) 2021 Utopic Panther
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
import opencc

from fgi.plugin import Plugin
from fgi.game import GameL10n

class ChineseConvertorPlugin(Plugin):
    def __init__(self, options):
        super().__init__(options)

        self.s2tw = opencc.OpenCC('s2twp.json')
        self.tw2s = opencc.OpenCC('tw2sp.json')

    def _conv(self, gctx, game, f, t, cc):
        with open(os.path.join(gctx.dbdir, "l10n", f, game.id + ".yaml")) as stream:
            data = yaml.safe_load(cc.convert(stream.read()))

        game.add_l10n_data(t, data, game.tr[f].mtime)

    def loader_pre_game_realize(self, gctx, game, *args, **kwargs):
        has_cn = "zh-cn" in game.tr
        has_tw = "zh-tw" in game.tr

        if has_cn and not has_tw:
            self._conv(gctx, game, "zh-cn", "zh-tw", self.s2tw)
        elif has_tw and not has_cn:
            self._conv(gctx, game, "zh-tw", "zh-cn", self.tw2s)

    def post_build(self, buildinfo_file, *args, **kwargs):
        buildinfo_file.write(f"zhconv: OpenCC version: {opencc.__version__}\n")

impl = ChineseConvertorPlugin
