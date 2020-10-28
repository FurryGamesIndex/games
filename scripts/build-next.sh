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

if [ -n "$(git status --porcelain)" ]; then
	echo "Working space MUST be clean while doing FGI-next build"
	echo "Exiting..."
	exit 1
fi

rm -f .patches_info

git branch --list "next-*" | while read -r branch ; do
	echo "applying $branch"
	git merge --no-ff --no-commit "$branch"
	git reset HEAD
done
git branch --list "next-*" | while read -r branch ; do
	git log --pretty='format:%H  %s' "..$branch" >> .patches_info
	echo '' >> .patches_info
done

mkdir -p extraui
cat > extraui/en.yaml <<EOF
infobar: >
  <i class="fas fa-exclamation-circle"></i> This is FGI-next, a unstable preview contains many changes that may be finally rejected. <a href="https://furrygamesindex.github.io/">Click here to switch to the stable version</a>
EOF
cat > extraui/zh-cn.yaml <<EOF
infobar: >
  <i class="fas fa-exclamation-circle"></i> 这是 FGI-next，一个 FGI 的实验性预览构建，可能包含很多最终被否决的更改。<a href="https://furrygamesindex.github.io/">点击此处切换到稳定版本</a>
EOF

./zhconv.py --no-builtin extraui/zh-cn.yaml:extraui/zh-tw.yaml
./generate.py --next --images-candidate-webp --no-sitemap --extra-ui extraui --with-rss "$1"

git reset --hard
git clean -f -d
