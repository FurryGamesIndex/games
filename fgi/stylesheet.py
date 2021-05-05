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

import re
import os
import yaml

class StyleSheet:
    def __init__(self, path, mtime, data):
        self.path = path
        self.mtime = mtime
        self.data = data

    def write_to_file(self, dirname):
        with open(os.path.join(dirname, self.path), "w") as f:
            f.write(self.data)

def _make_stylesheet_v1(indir):
    print(f"stylesheet_v1: loading {indir}")

    stylesheets = dict()

    for i in os.listdir(indir):
        fn = os.path.join(indir, i)
        with open(fn) as f:
            stylesheets[i] = StyleSheet(i, int(os.path.getmtime(fn)), f.read())

    return stylesheets

def _make_stylesheet_v2(indir, config):
    macros = config["macros"]
    stylesheets = dict()

    for i in config["stylesheets"]:
        fn = i["output"]
        mtime = 0
        print(f"stylesheet_v2: {indir}: creating {fn}")

        data = ""
        for infile in i["input"]:
            ifn = os.path.join(indir, infile) 

            imtime = int(os.path.getmtime(ifn))
            if imtime > mtime:
                mtime = imtime

            with open(ifn) as f:
                data = data + "\n\n" + f.read()

        for name, value in macros.items():
            data = re.sub(r"\$" + name + r"([ :;\)])", value + r"\1", data)

        undefined_macros = re.findall(r"\$([a-zA-Z_-]+)[ :;\)]", data)
        if undefined_macros:
            for m in undefined_macros:
                print(f"[error] {i['output']}: undefined macro: {m}")
            raise ValueError("Undefined macros")

        stylesheets[fn] = StyleSheet(fn, mtime, data)

    return stylesheets

def make_stylesheet(indir):
    v2_fn = os.path.join(indir, "stylesheet_v2.yaml")
    if os.path.exists(v2_fn):
        with open(v2_fn) as f:
            return _make_stylesheet_v2(indir, yaml.safe_load(f))
    else:
        return _make_stylesheet_v1(indir)

__all__ = [ "make_stylesheet" ]
