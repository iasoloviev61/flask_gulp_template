#!/usr/bin/env bash
# usage ./create-block.sh blockname
SOURCEPATH="../appdata/frontend/source/blocks/"
mkdir -p $SOURCEPATH$1
cp template/template.pug $SOURCEPATH$1/$1.pug
cp template/template.js $SOURCEPATH$1/$1.js
cp template/_template.scss $SOURCEPATH$1/_$1.scss
echo "@import \"../blocks/$1/$1\";" >> ../appdata/frontend/source/style/main.scss