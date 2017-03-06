#!/bin/bash

echo ""
echo "Comitting raw post(s) to git (master-branch)"
echo ""
git add ./posts/
git commit -m "Version auto-comitted"
git push

echo ""
echo "**************************"
echo ""
echo "(Re-)gererating site ..."
echo ""
python chisel.py

echo ""
echo "**************************"
echo ""
echo "Updating gh-pages ..."
echo ""
ghp-import -n -c "log.logiskhave.dk" -m "Site updated" -p ./www/
