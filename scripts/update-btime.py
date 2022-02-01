#!/usr/bin/env python3

import os
import sys
import json
import subprocess

os.environ["LANG"] = "C.UTF-8"
os.environ["LANGUAGE"] = ""
os.environ["LC_ALL"] = ""

def get_btime_from_git(fn):
    cmd = [ "git", "log", "--diff-filter=A", "--follow", "--format=%ct", "-1", "--", fn ]
    btime_str = subprocess.check_output(cmd).decode('utf-8').rstrip()
    btime = int(btime_str)

    if btime == 0:
        raise ValueError("birth time is zero!")

    return btime

if len(sys.argv) < 3:
    print(f"usage: {sys.argv[0]} <games dir> <output filename>")
    sys.exit(-1)

dirname = sys.argv[1]
output = sys.argv[2]

data = {}
try:
    if os.path.exists(output):
        with open(output) as f:
            data = json.load(f)
except:
    data = {}

for f in os.listdir(dirname):
    fn = os.path.join(dirname, f)
    if os.path.isfile(fn) and f.endswith(".yaml"):
        game_id = os.path.splitext(f)[0]
        if game_id not in data:
            print(f"=> {game_id}")
            data[game_id] = get_btime_from_git(fn)

with open(output, "w") as f:
    json.dump(data, f, ensure_ascii=False)
