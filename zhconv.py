#!/usr/bin/env python3
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
from opencc import OpenCC

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--opencc-profile', type=str, help='Use specify OpenCC profile(not impl)')
parser.add_argument('--no-builtin', default=False, action='store_true', help='Do not run builtin path conv')
parser.add_argument('--builtin-reverse', default=False, action='store_true', help='zh-tw to zh-cn for builtin dir conv(not impl)')
parser.add_argument('extra_pathes', type=str, default=[], help='add extra path', nargs="*")

args = parser.parse_args()

root_dir = "."
games_dir = os.path.join("games", "l10n")
uil10n_dir = "uil10n"
doc_dir = "doc"

converter = OpenCC('s2twp.json')
origin = "zh-cn"
to = "zh-tw"

def conv(of, tf, fixlinks = False):
    print("Converting %s, fixlinks=%r" % (of, fixlinks))
    with open(of) as stream:
        data = converter.convert(stream.read())

    if fixlinks:
        data = data.replace("." + origin + ".", "." + to + ".")
        data = data.replace("/" + origin + "/", "/" + to + "/")

    with open(tf, 'w') as stream:
        stream.write(data)

def convdir(od, td):
	for f in os.listdir(od):
	    file = os.path.join(od, f)
	    if (not os.path.isfile(file)) or (f[0] == '.'):
                continue

	    conv(file, os.path.join(td, f))

if not args.no_builtin:
    convdir(os.path.join(games_dir, origin), os.path.join(games_dir, to))
    conv(os.path.join(uil10n_dir, origin + ".yaml"), os.path.join(uil10n_dir, to + ".yaml"), True)
    conv(os.path.join(root_dir, "README.%s.md" % origin), os.path.join(root_dir, "README.%s.md" % to), True)
    conv(os.path.join(doc_dir, "Contribute.%s.md" % origin), os.path.join(doc_dir, "Contribute.%s.md" % to), True)
#    conv(os.path.join(doc_dir, "tags.%s.md" % origin), os.path.join(doc_dir, "tags.%s.md" % to), True)
    conv(os.path.join(doc_dir, "faq.%s.md" % origin), os.path.join(doc_dir, "faq.%s.md" % to), True)

for i in args.extra_pathes:
    f = i.split(":")[0]
    t = i.split(":")[1]
    if os.path.isfile(f):
        conv(f, t)
    elif os.path.isdir(f):
        convdir(f, t, True)
    else:
        print("Warning: unknown path: %s" % f)
