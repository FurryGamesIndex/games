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
from ruamel.yaml import YAML
from importlib.metadata import version

yaml = YAML(typ="safe")
from fgi.plugin import Plugin


class ChineseConvertorPlugin(Plugin):
    def __init__(self, options):
        self.critical = False

        super().__init__(options)

        self.drop_zh = False
        self.opencc_version = "N/A"

        try:
            import opencc

            self.s2tw = opencc.OpenCC("s2twp.json")
            self.tw2s = opencc.OpenCC("tw2sp.json")

            self.opencc_version = version("opencc")

        except Exception as e:
            if self.critical:
                raise e
            else:
                print("[warning] zhconv: opencc load failed, zhconv disabled")
                print("[warning] zhconv: disabling zh-cn, zh-tw build")
                self.drop_zh = True

    def i18n_post_ll_done(self, ll, *args, **kwargs):
        if self.drop_zh:
            return [l for l in ll if l != "zh-cn" and l != "zh-tw"]
        else:
            return ll

    def _conv(self, gctx, game, f, t, cc):
        with open(os.path.join(gctx.dbdir, "l10n", f, game.id + ".yaml")) as stream:
            data = yaml.load(cc.convert(stream.read()))

        game.add_l10n_data(t, data, game.tr[f].mtime)

    def loader_pre_game_realize(self, gctx, game, *args, **kwargs):
        has_cn = "zh-cn" in game.tr
        has_tw = "zh-tw" in game.tr

        if has_cn and not has_tw:
            self._conv(gctx, game, "zh-cn", "zh-tw", self.s2tw)
        elif has_tw and not has_cn:
            self._conv(gctx, game, "zh-tw", "zh-cn", self.tw2s)

    def post_build(self, buildinfo_file, *args, **kwargs):
        buildinfo_file.write(f"zhconv: OpenCC version: {self.opencc_version}\n")


impl = ChineseConvertorPlugin
