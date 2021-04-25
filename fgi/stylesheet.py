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
from distutils import dir_util

def _make_stylesheet_v1(indir, outdir):
    print(f"stylesheet_v1: copy {indir}")
    dir_util.copy_tree(indir, outdir)

def _make_stylesheet_v2(indir, config, outdir):
    macros = config["macros"]

    for i in config["stylesheets"]:
        fn = i["output"]
        print(f"stylesheet_v2: {indir}: create {fn}")

        data = ""
        for infile in i["input"]:
            with open(os.path.join(indir, infile)) as f:
                data = data + "\n\n" + f.read()

        for name, value in macros.items():
            data.replace("$" + name, value)

        with open(os.path.join(outdir, fn), "w") as of:
            of.write(data)

def make_stylesheet(indir, outdir):
    v2_fn = os.path.join(indir, "stylesheet_v2.yaml")
    if os.path.exists(v2_fn):
        with open(v2_fn) as f:
            return _make_stylesheet_v2(indir, yaml.safe_load(f), outdir)
    else:
        return _make_stylesheet_v1(indir, outdir)

__all__ = [ "make_stylesheet" ]
