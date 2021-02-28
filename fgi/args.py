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

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--extra-ui', type=str, help='Set extra ui profile path')
parser.add_argument('--no-sitemap', default=False, action='store_true', help='Do not generate sitemap')
parser.add_argument('--no-searchdb', default=False, action='store_true', help='Do not generate searchdb')
parser.add_argument('--no-sub-lists', default=False, action='store_true', help='Do not render sub lists')
parser.add_argument('--no-purge-prev-builds', default=False, action='store_true', help='Do not purge previous builds')
parser.add_argument('--download-external-images', default=False, action='store_true', help='Download external images to output dir')
parser.add_argument('--use-external-images-cache', type=str, help='Set a previous builds dir to avoid to download repeatly')
parser.add_argument('--images-to-webp', default=False, action='store_true', help='convert images to webp and replace original (cwebp command required)')
parser.add_argument('--images-candidate-webp', default=False, action='store_true', help='convert images to webp as candidation (cwebp command required)')
parser.add_argument('--with-rss', default=False, action='store_true', help='generate RSS feeds (need to run scripts/fix-mtime.sh first)')
parser.add_argument('--file-uri-workaround', default=False, action='store_true', help='Generate workaround files to make site work well on file://')
parser.add_argument('--next', default=False, action='store_true', help='enable experimental features')
parser.add_argument('--data-dir-prefix', default="", type=str, help='Specify the where the FGI datas stored (defaultly current directory)')
parser.add_argument('--plugin', type=str, action='append', help='Load plugin. format: name[,options] (To load multiple plugins, you can specify this argument multiple times)')
parser.add_argument('output', type=str, help='Output path')

def parse(argv):
    return parser.parse_args(argv)
