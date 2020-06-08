# -*- coding: utf-8 -*-

import requests

req_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0"
}

def dl(uri, path):
    data = requests.get(uri, headers=req_headers).content
    with open(path, "wb") as f:
        f.write(data)

if __name__ == "__main__":
    from sys import argv
    dl(argv[1], "/var/tmp/test")
