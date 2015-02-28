#!/bin/bash
# cd to build folder gh pages and add/commit/push changes to gh-pages branch
cd gh-pages
git add -A
git commit -a -m "updated"
git push
cd ../
