#!/usr/bin/env bash

nl=$'\n'

[ -z "$BASE_REF" ] && BASE_REF="${SHA}~1"

games=$(git diff --name-only --diff-filter=A "${BASE_REF}" "${SHA}" | grep '^games/' | sed 's|games/\([^.]*\).yaml|<a href="furrygamesindex.github.io/zh-cn/games/\1.html">\1</a>|g')
if [ -n "$games" ]; then
	curl "https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage" --data-urlencode "chat_id=${TELEGRAM_TO}" --data-urlencode "disable_web_page_preview=true" --data-urlencode "parse_mode=html" --data-urlencode "text=[Github] 已添加游戏：${nl}${games}" > /dev/null
else
	echo "No games added"
fi

exit 0
