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
	echo "Running git status..."
	git status
	echo "Exiting..."
	exit 1
fi

rm -f .patches_info

die() {
	echo "$1"
	exit 2
}

init() {
	test -z "$1" && die "missing remote name"
	git branch -r --list "$1/next-*" | while read -r branch ; do
		lb="${branch#*/}"
		echo "create local branch $lb"
		git branch "$lb" "${branch}"
	done

}

build() {
	git branch --list "next-*" | while read -r branch ; do
		git log --pretty='format:%H  %s' "..$branch" --reverse >> .patches_info
		echo '' >> .patches_info
	done

	cat .patches_info | while read -r i ; do
		echo "Applying patch $i"
		i="${i%% *}"
		git diff-tree -p --binary "$i" | git apply
	done

	mkdir -p extraui
	cat > extraui/en.yaml <<EOF
infobar: >
  This is FGI-next, experimental preview build of FGI, which may contain many changes that are under testing and may even be broken. <a href="https://furrygames.top/">Switch to stable version</a>
EOF
	cat > extraui/zh-cn.yaml <<EOF
infobar: >
  这是 FGI-next，FGI 的实验性预览构建，它可能包含很多正在测试中的改动，甚至可能会影响正常使用。<a href="https://furrygames.top/">切换到稳定版本</a>
EOF
	cat > extraui/zh-tw.yaml <<EOF
infobar: >
  這是 FGI-next，FGI 的實驗性預覽構建，它可能包含很多正在測試中的改動，甚至可能會影響正常使用。<a href="https://furrygames.top/">切換到穩定版本</a>
EOF

	UIMOD=""
	if [ -d staging-ui ]; then
		echo "staging-ui detected, uimod plugin will be loaded."
		UIMOD="--plugin uimod,mod=staging-ui"
	fi

	./generate.py --next \
		--images-candidate-webp \
		--no-sitemap \
		--extra-ui extraui \
		--with-rss \
		$UIMOD \
		--plugin steam-cdn-unite,verbose=1 "$1"
	cat > "$1/robots.txt" <<EOF
User-agent: *
Disallow: /
EOF
}

action="$1"

case "$action" in
init)
	init "${2}"
	;;
build)
	build "${2:-output-next}"
	;;
clean-tree)
	;;
*)
	cat <<EOF
usage: build-next.sh <action> [arguments ...]

	init <remote name>
	build [output path]
	clean-tree
EOF
	;;
esac

git reset --hard
git clean -f -d
