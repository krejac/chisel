#!/bin/bash

echo ""
echo "Activating Python environment"
source ./venv/bin/activate

echo ""
echo "**************************"
echo ""
echo "Comitting raw post(s) to git (master-branch)"
echo ""
git add ./posts/
git commit -m "Version auto-comitted :robot:"
git push

echo ""
echo "**************************"
echo ""
echo "(Re-)generating site ..."
echo ""
python chisel.py

echo ""
echo "**************************"
echo ""
echo "Copying static files ..."
echo ""
cp -r ./static/ ./www/static/
mkdir -p ./www/css/ && cp ./theme/theme.css ./www/css/

echo ""
echo "**************************"
echo ""
echo "Updating gh-pages ..."
echo ""
ghp-import -n -c "log.logiskhave.dk" -m "Site updated :rocket:" -p ./www/

echo ""
echo "**************************"
echo ""
echo "Deactivating Python environment"
echo ""
deactivate
