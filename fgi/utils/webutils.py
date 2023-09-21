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

import requests
from urlparse import urlparse
req_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0"
}


def dl(uri, path):
    data = requests.get(uri, headers=req_headers).content
    with open(path, "wb") as f:
        f.write(data)


def patch_unavailable_cdn(url: str):
    if 'media.st.dl.pinyuncloud.com' in url:
        return url.replace('media.st.dl.pinyuncloud.com', "cdn.cloudflare.steamstatic.com")
    return url

if __name__ == "__main__":
    from sys import argv

    dl(argv[1], "/var/tmp/test")
