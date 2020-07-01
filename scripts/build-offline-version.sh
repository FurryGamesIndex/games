#!/usr/bin/env bash

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

RMRF="rm -rf "
[ "$(uname -s)" = "Linux" ] && RMRF="$RMRF --preserve-root"

OUTPUT_DIR="${1:-output}"
echo "Output directory is $OUTPUT_DIR"

if [ -d "$OUTPUT_DIR" ]; then
	mv "${OUTPUT_DIR}/assets" "/var/tmp/fgi_assets"
	${RMRF} "${OUTPUT_DIR}"
	mkdir -p "${OUTPUT_DIR}"
	mv "/var/tmp/fgi_assets" "${OUTPUT_DIR}/assets"
	echo "cleaned prev builds dir without assets"
fi

mkdir -p extraui
dt=$(date -R)
cat > extraui/en.yaml <<EOF
infobar: >
  <i class="fas fa-exclamation-circle"></i> This is a snapshot offline built for FurryGamesIndex (Build datetime: ${dt}). The upstream online version may already have a lot of improvements. <a href="https://furrygamesindex.github.io/">Click here to switch to the online version</a>
search_extra_scripts: >
  <script src="../scripts/searchdb_offline.js"></script>
EOF
cat > extraui/zh-cn.yaml <<EOF
infobar: >
  <i class="fas fa-exclamation-circle"></i> 这是一个 FurryGamesIndex 的离线快照构建（构建时间：${dt}）。上游在线版本可能已经有了重大改进。<a href="https://furrygamesindex.github.io/">点击此处切换到在线版本</a>
EOF

./zhconv.py --no-builtin extraui/zh-cn.yaml:extraui/zh-tw.yaml
./generate.py --no-sitemap --no-purge-prev-builds --download-external-images --extra-ui extraui "$OUTPUT_DIR"

echo -n "var _searchdb=JSON.parse(atob('" > "${OUTPUT_DIR}/scripts/searchdb_offline.js"
cat "${OUTPUT_DIR}/scripts/searchdb.json" | python3 -m base64 | tr -d "\n" >> "${OUTPUT_DIR}/scripts/searchdb_offline.js"
echo -n "'))" >> "${OUTPUT_DIR}/scripts/searchdb_offline.js"
