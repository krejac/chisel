#!/bin/bash

echo ""
echo "(Re-)gererating site ..."
echo ""
python chisel.py

echo ""
echo "Updating gh-pages ..."
echo ""
ghp-import -n -c "log.logiskhave.dk" -m "Site updated" -p ./www/
