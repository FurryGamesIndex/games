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

from fgi.plugin import Plugin
from fgi.utils import webp

# STUB Webp converting but let FGI But think webp had converted.
# 
# This allows the HTML picture to have a webp source, but without
# actually doing the conversion to get a very fast build speed.
# 
# This is useful at times, for example for debugging purposes.
# Or for the benefit of the cn-optimize plugin.

class WebpConverterSTUBPlugin(Plugin):
    def __init__(self, options):
        self._bypass_hook_chain = True
        super().__init__(options)

        assert webp.cwebp_impl is None
        webp.cwebp_impl = self

    def webp_converter_impl(self, ofn, tfn):
        pass

impl = WebpConverterSTUBPlugin
