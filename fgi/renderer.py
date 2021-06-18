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

class Renderer:
    def __init__(self, fctx, lctx, nonl10n = False):
        self.fctx = fctx
        self.nonl10n = nonl10n

        self.env = fctx.env
        self.lctx = lctx

        if nonl10n:
            self.basectx["lang"] = "en"
        else:
            self.language = lctx["lang"]
            langtag = self.language.split('-')

            self.lang_without_region = langtag[0]
            self.basectx["lang_without_region"] = self.lang_without_region

            lang_unix_style = self.lang_without_region
            lang_bcp47 = self.lang_without_region
            if len(langtag) >= 2:
                lang_unix_style += "_" + langtag[1].upper()
                lang_bcp47 += "-" + langtag[1].upper()

            self.basectx["lang_unix_style"] = lang_unix_style
            self.basectx["lang_bcp47"] = lang_bcp47

    def new_context(self):
        context = self.basectx.copy()
        context.update(self.lctx)
        return context

    def getpath(self, *fn):
        if self.nonl10n:
            return os.path.join(self.fctx.output, *fn)
        else:
            return os.path.join(self.fctx.output, self.language, *fn)

    def getpath_sm(self, *fn):
        path = "/".join([*fn])

        if not self.nonl10n:
            path = self.language + "/" + path

        return path

    def sm_openw(self, *fn, sm = True, **kwargs):
        if sm:
            self.fctx.sitemap.add_entry(self.getpath_sm(*fn), **kwargs)
        return open(self.getpath(*fn), "w")

    def render(self):
        pass
