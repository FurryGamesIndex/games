#!/usr/bin/env python3

import os
import sys

sys.path.insert(0, os.getcwd())

from fgi import stylesheet

r = stylesheet.make_stylesheet(sys.argv[1])
for _, ss in r.items():
    ss.write_to_file(sys.argv[2])
