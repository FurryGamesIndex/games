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

nl=$'\n'

BASE_REF=$(jq --raw-output .commits[0].id "$GITHUB_EVENT_PATH")
END_REF=$(jq --raw-output .commits[-1].id "$GITHUB_EVENT_PATH")

echo "BASE_REF: $BASE_REF"
echo "END_REF: $END_REF"

#[ "$BASE_REF" = "$END_REF" ] && BASE_REF="${END_REF}~1"
BASE_REF="${BASE_REF}~1"

games=$(git diff --name-only --diff-filter=A "${BASE_REF}" "${END_REF}" | grep '^games/[^/]*.yaml' | sed 's|games/\([^.]*\).yaml|<a href="https://furrygamesindex.github.io/zh-cn/games/\1.html">\1</a>|g')

echo "$games"

if [ -n "$games" ]; then
	curl "https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage" --data-urlencode "chat_id=${TELEGRAM_TO}" --data-urlencode "disable_web_page_preview=true" --data-urlencode "parse_mode=html" --data-urlencode "text=[Github] 已添加游戏：${nl}${games}${nl}${nl}需要等待 1 分钟或更长的时间后才能访问" > /dev/null
else
	echo "No games added"
fi

exit 0
