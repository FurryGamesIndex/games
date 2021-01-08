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

games=$(git diff --name-only --diff-filter=A "${BASE_REF}" "${END_REF}" | grep '^games/[^/]*.yaml' | sed 's|games/\([^.]*\).yaml|\1|g')

games_zh=""
games_en=""

IFS="$nl"
while read -r i ; do
	echo "new: $i"
	uri="https://furrygames.top/zh-cn/games/${i}.html"
	uri_en="https://furrygames.top/en/games/${i}.html"
	grep '^expunge:' "games/$i.yaml" > /dev/null 2>&1
	[ "$?" = "0" ] && i="$i (Expunged)"
	grep '^replaced-by:' "games/$i.yaml" > /dev/null 2>&1
	[ "$?" = "0" ] && i="$i (Be Replaced)"
	games_zh="${games_zh}<a href='${uri}'>${i}</a>${nl}"
	games_en="${games_en}<a href='${uri_en}'>${i}</a>${nl}"
done <<< "$games"

echo "$games_zh"

if [ -n "$games" ]; then
	curl "https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage" --data-urlencode "chat_id=${TELEGRAM_TO}" --data-urlencode "disable_web_page_preview=true" --data-urlencode "parse_mode=html" --data-urlencode "text=[Github] 已添加游戏：${nl}${games_zh}${nl}<i>需要等待 1 分钟或更长的时间后才能访问</i>" > /dev/null
	sleep 1
	curl "https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage" --data-urlencode "chat_id=${TELEGRAM_TO_EN}" --data-urlencode "disable_web_page_preview=true" --data-urlencode "parse_mode=html" --data-urlencode "text=[Github] Game added：${nl}${games_en}${nl}<i>Wait 1 minute or more before accessing</i>" > /dev/null
else
	echo "No games added"
fi

exit 0
