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

import yaml
from sys import argv
from pprint import pprint

lang = argv[1]

uilang = {
    'en': {
        'namespace': '## Namespace %s',
        'tip': 'If you want to add new tags, welcome to create issues for discussion.'
    },
    'zh-cn': {
        'namespace': '## %s 命名空间',
        'tip': '如果你认为应该增加新的标签，欢迎创建 issues 讨论。'
    }
}

def _doctag_content(data):
    if "content" in data:
        for blk in data["content"]:
            print(blk.get(lang, blk["en"]))
            print()

def doctag_namespace(name, data):
    print()
    print(uilang[lang]["namespace"] % data["name"])
    print()
    _doctag_content(data)

def doctag_class(name, data):
    print()
    print("### %s" % data["title"].get(lang, data["title"]["en"]))
    print()
    _doctag_content(data)

def doctag_tag(name, data):
    print("- `%s` %s" % (name, data["explanation"].get(lang, data["explanation"]["en"])))

with open("tags.yaml") as f:
    tags = yaml.safe_load(f.read())

doctag_funcs = {
    '@namespace': doctag_namespace,
    '@class': doctag_class
}

print("# Tags")
print()
print(uilang[lang]["tip"])
for key in tags:
    if key[0] == "@":
        func = key.split(':')[0]
        doctag_funcs[func](key, tags[key])
    else:
        doctag_tag(key, tags[key])
