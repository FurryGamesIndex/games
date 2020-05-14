#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from opencc import OpenCC

games_dir = os.path.join("games", "l10n")
uil10n_dir = "uil10n"
doc_dir = "doc"

converter = OpenCC('s2twp.json')
origin = "zh-cn"
to = "zh-tw"

def conv(of, tf):
    print("Converting %s" % of)
    with open(of) as stream:
        data = converter.convert(stream.read())

    with open(tf, 'w') as stream:
        stream.write(data)

def convdir(od, td):
	for f in os.listdir(od):
	    file = os.path.join(od, f)
	    if (not os.path.isfile(file)) or (f[0] == '.'):
                continue

	    conv(file, os.path.join(td, f))

convdir(os.path.join(games_dir, origin), os.path.join(games_dir, to))
conv(os.path.join(uil10n_dir, origin + ".yaml"), os.path.join(uil10n_dir, to + ".yaml"))
conv(os.path.join(doc_dir, "Contribute.%s.md" % origin), os.path.join(doc_dir, "Contribute.%s.md" % to))
conv(os.path.join(doc_dir, "tags.%s.md" % origin), os.path.join(doc_dir, "tags.%s.md" % to))
