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
import argparse
import yaml
from opencc import OpenCC

parser = argparse.ArgumentParser()
parser.add_argument('--no-builtin', default=False, action='store_true', help='Do not run builtin path conv')
parser.add_argument('extra_pathes', type=str, default=[], help='add extra path', nargs="*")

args = parser.parse_args()

root_dir = "."
games_dir = os.path.join("games", "l10n")
uil10n_dir = "uil10n"
doc_dir = "doc"

converter = OpenCC('s2twp.json')
origin = "zh-cn"
to = "zh-tw"

convertert2s = OpenCC('tw2sp.json')

def conv(of, tf, fixlinks = False, conv=converter):
    print("Converting %s, fixlinks=%r" % (of, fixlinks))
    with open(of) as stream:
        data = conv.convert(stream.read())

    if conv is not converter and fixlinks:
        raise NotImplementedError("fix links is not implemented for non-default converter")

    if fixlinks:
        data = data.replace("." + origin + ".", "." + to + ".")
        data = data.replace("/" + origin + "/", "/" + to + "/")

    with open(tf, 'w') as stream:
        stream.write(data)

def __convgamesl10n(cn, tw, f, fn):
    cnf = os.path.join(cn, f)
    twf = os.path.join(tw, f)

    with open(fn) as stream:
        data = yaml.safe_load(stream)

    if "X-Chinese-Convertor-Hint" in data:
        data = data["X-Chinese-Convertor-Hint"]
        if "prefer" in data:
            if data["prefer"] == "TW":
                conv(twf, cnf, conv=convertert2s)
            elif data["prefer"] == "CN":
                conv(cnf, twf)
            elif data["prefer"] == "ignored":
                pass
            else:
                raise ValueError("unsupported cchint prefer %s" % prefer)
    else:
        conv(cnf, twf)

def convgamesl10n(cn, tw):
    cnfiles = [i for i in os.listdir(cn) if os.path.isfile(os.path.join(cn, i)) and i[0] != '.']
    for f in cnfiles:
        fn = os.path.join(cn, f)
        __convgamesl10n(cn, tw, f, fn)

    twfiles = [i for i in os.listdir(tw) \
                if os.path.isfile(os.path.join(tw, i)) and \
                i[0] != '.' and \
                i not in cnfiles]
    for f in twfiles:
        print("New TW file: %s" % f)
        fn = os.path.join(tw, f)
        __convgamesl10n(cn, tw, f, fn)


if not args.no_builtin:
    convgamesl10n(os.path.join(games_dir, origin), os.path.join(games_dir, to))
    conv(os.path.join(uil10n_dir, origin + ".yaml"), os.path.join(uil10n_dir, to + ".yaml"), True)
    conv(os.path.join(root_dir, "README.%s.md" % origin), os.path.join(root_dir, "README.%s.md" % to), True)

    conv(os.path.join(doc_dir, "Get-Involved.%s.md" % origin), os.path.join(doc_dir, "Get-Involved.%s.md" % to), True)
    conv(os.path.join(doc_dir, "FGI-members.%s.md" % origin), os.path.join(doc_dir, "FGI-members.%s.md" % to), True)
    conv(os.path.join(doc_dir, "Contribute.%s.md" % origin), os.path.join(doc_dir, "Contribute.%s.md" % to), True)
    conv(os.path.join(doc_dir, "contribute_guide", "patches-submitting.%s.md" % origin), os.path.join(doc_dir, "contribute_guide", "patches-submitting.%s.md" % to), True)
    conv(os.path.join(doc_dir, "contribute_guide", "zhconv.%s.md" % origin), os.path.join(doc_dir, "contribute_guide", "zhconv.%s.md" % to), False)
    conv(os.path.join(doc_dir, "contribute_guide", "game.%s.md" % origin), os.path.join(doc_dir, "contribute_guide", "game.%s.md" % to), True)

    conv(os.path.join(doc_dir, "faq.%s.md" % origin), os.path.join(doc_dir, "faq.%s.md" % to), True)
    conv(os.path.join(doc_dir, "search_help.%s.md" % origin), os.path.join(doc_dir, "search_help.%s.md" % to), True)

for i in args.extra_pathes:
    f = i.split(":")[0]
    t = i.split(":")[1]
    if os.path.isfile(f):
        conv(f, t)
    else:
        raise ValueError("file not exists: %s" % f)
