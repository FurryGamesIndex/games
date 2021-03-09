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

from fgi.plugin import Plugin

class UIModPlugin(Plugin):
    def __init__(self, options):
        self.mod = None
        super().__init__(options)

        print("FGI UI mod loader plugin")
        print(f"Loading mod: {self.mod}")

    def global_pre_initialization(self, gctx):
        if not os.path.isdir(self.mod):
            raise ValueError(f"'{self.mod}' is not a directory")

        dir_templates = os.path.join(self.mod, "templates")
        if os.path.isdir(dir_templates):
            gctx.dir_templates.insert(0, dir_templates)

        dir_styles = os.path.join(self.mod, "styles")
        if os.path.isdir(dir_styles):
            gctx.styles_path.insert(0, dir_styles)

impl = UIModPlugin
