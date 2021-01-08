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
        self.basectx = None
        self.nonl10n = nonl10n

        self.env = fctx.env
        self.lctx = lctx

        if not nonl10n:
            self.language = lctx["lang"]

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
        path = self.getpath()
        return path, "/".join([*fn])

    def render(self):
        pass
