#!/usr/bin/env bash

mkdir -p extraui
dt=$(date -R)
cat > extraui/en.yaml <<EOF
infobar: >
  <i class="fas fa-exclamation-circle"></i> This is a snapshot offline built for FurryGamesIndex (Build datetime: ${dt}). The upstream version may already have a lot of improvements. Click the link to enter the online version: <a href="https://furrygamesindex.github.io/">https://furrygamesindex.github.io/</a>
EOF
cat > extraui/zh-cn.yaml <<EOF
infobar: >
  <i class="fas fa-exclamation-circle"></i> 这是一个 FurryGamesIndex 的离线快照构建（构建时间：${dt}）。上游版本可能已经有了重大改进。点击此链接进入在新版本：<a href="https://furrygamesindex.github.io/">https://furrygamesindex.github.io/</a>
EOF
./zhconv.py --no-builtin extraui/zh-cn.yaml:extraui/zh-tw.yaml
./generate.py --no-sitemap --extra-ui extraui "${1:-output}"
