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

lang = argv[1]

uilang = {
    'en': {
        'namespace': '## Namespace %s',
        'tip': 'If you want to add new tags, welcome to create issues for discussion.',
        'alias': 'This tag has these alias(es): ',
        'implication': 'This tag implicate (depend on) these tags: ',
    },
    'zh-cn': {
        'namespace': '## %s 命名空间',
        'tip': '如果你认为应该增加新的标签，欢迎创建 issues 讨论。',
        'alias': '此标签有这些别名：',
        'implication': '此标签蕴含（依赖）这些标签: ',
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
    explan = data["explanation"].get(lang, data["explanation"]["en"])

    print(f"- `{name}` {explan}")

    if "alias" in data:
        aliases = uilang[lang]["alias"] + "`" + "`, `".join(data["alias"]) + "`"
        print(f"    - {aliases}")

    if "implication" in data:
        implications = uilang[lang]["implication"] + "`" + "`, `".join(data["implication"]) + "`"
        print(f"    - {implications}")
    elif name in extra_tagdep:
        implications = uilang[lang]["implication"] + "`" + "`, `".join(extra_tagdep[name]) + "`"
        print(f"    - {implications}")

with open("tags.yaml") as f:
    tags = yaml.safe_load(f.read())

extra_tagdep = dict()
with open("tag-dependencies.yaml") as f:
    tagdep2 = yaml.safe_load(f.read())
    for _, v in tagdep2.items():
        for tag, i in v.items():
            extra_tagdep[tag] = i

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
