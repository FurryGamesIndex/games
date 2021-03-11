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

set -e

RMRF="rm -rf "
[ "$(uname -s)" = "Linux" ] && RMRF="$RMRF --preserve-root"

OUTPUT_DIR="${1:-output}"
OUTPUT_DIR_WEBP="${1:-output}-webp"
CACHE_DIR="${2:-output}"
echo "Output directory is $OUTPUT_DIR"
echo "Cache directory is $CACHE_DIR"

#if [ -d "$OUTPUT_DIR" ]; then
#	mv "${OUTPUT_DIR}/assets" "/var/tmp/fgi_assets"
#	${RMRF} "${OUTPUT_DIR}"
#	mkdir -p "${OUTPUT_DIR}"
#	mv "/var/tmp/fgi_assets" "${OUTPUT_DIR}/assets"
#	echo "cleaned prev builds dir without assets"
#fi

mkdir -p extraui
dt=$(date -R)
cat > extraui/en.yaml <<EOF
infobar: >
  This is a snapshot offline built for FurryGamesIndex (Build datetime: ${dt}). The upstream online version may already have a lot of improvements. <a href="https://furrygames.top/">Click here to switch to the online version</a>
EOF
cat > extraui/zh-cn.yaml <<EOF
infobar: >
  这是一个 FurryGamesIndex 的离线快照构建（构建时间：${dt}）。上游在线版本可能已经有了重大改进。<a href="https://furrygames.top/">点击此处切换到在线版本</a>
EOF
cat > extraui/zh-tw.yaml <<EOF
infobar: >
  這是一個 FurryGamesIndex 的離線快照構建（構建時間：${dt}）。上游線上版本可能已經有了重大改進。<a href="https://furrygames.top/">點選此處切換到線上版本</a>
EOF

./generate.py --no-sitemap --file-uri-workaround --download-external-images --use-external-images-cache "$CACHE_DIR" --extra-ui extraui "$OUTPUT_DIR"
test "$FGI_OFFLINE_WEBP" = 1 && ./generate.py --no-sitemap --file-uri-workaround --download-external-images --images-to-webp --use-external-images-cache "$OUTPUT_DIR" --extra-ui extraui "$OUTPUT_DIR_WEBP"
