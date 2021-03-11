#!/usr/bin/env bash

DATE="gdate"
[ "$(uname -s)" = "Linux" ] && DATE="date"

git ls-tree -r --name-only HEAD | while read filename; do 
	unixtime=$(git log -1 --format="%at" -- "${filename}")

	# do not makes lastmod smaller than first lastmod in sitemap.xml, hacking!
	test "$unixtime" -lt "1599510461" && unixtime=1599510461

	touchtime=$($DATE -d @$unixtime +'%Y%m%d%H%M.%S')
	touch -t ${touchtime} "${filename}"
done
