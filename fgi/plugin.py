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

import importlib

class Plugin:
    def __init__(self, options):
        if options:
            self._parse_options(options)

    def _update_option_attr(self, name, value):
        if hasattr(self, name):
            origin = getattr(self, name)
            if type(origin) is bool:
                if value == "false" or \
                        value == "0" or \
                        value == "no" or \
                        value == "OFF":
                    value = False
                elif value == "true" or \
                        value == "1" or \
                        value == "yes" or \
                        value == "ON":
                    value = True
                else:
                    raise ValueError(f"invalid boolean value '{value}'")
                setattr(self, name, value)
            elif type(origin) is str or origin is None:
                setattr(self, name, value)
            elif type(origin) is int:
                setattr(self, name, int(value))
            else:
                raise ValueError(f"Not supported option type {type(origin)}")
        else:
            raise NameError(f"Plugin does not support option {name}")

    def _parse_options(self, options):
        opts = options.split(",")
        for i in opts:
            pair = i.split("=", 1)
            name = pair[0]
            if name:
                if len(pair) == 2:
                    self._update_option_attr(name, pair[1])
                else:
                    self._update_option_attr(name, "true")


class PluginManager:
    def __init__(self):
        self.plugins = []

    def invoke_plugins(self, method, var, *args, **kwargs):
        for i in self.plugins:
            func = getattr(i, method, None)

            if func is None:
                continue

            _var = func(var, *args, **kwargs)
            if _var is not None:
                var = _var

        return var

    def load_plugin(self, name, options):
        p = importlib.import_module(".plugins." + name, package=__package__)
        if not hasattr(p, "impl"):
            raise ValueError(f"Module '{name}' does not provide a plugin implement.")
        plugin = p.impl(options)
        if not hasattr(plugin, "_bypass_hook_chain"):
            self.plugins.append(plugin)
