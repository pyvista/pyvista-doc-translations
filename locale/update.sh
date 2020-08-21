#!/bin/sh
# update transifex pot and local po files

set -ex

# required environment variables
# SPHINXINTL_TRANSIFEX_USERNAME=tkoyama010
# SPHINXINTL_TRANSIFEX_PROJECT_NAME=pyvista-doc
LOCAL_PYTHON_PATH="/home/runner/work/.venv/bin"

# pull po files from transifex
cd `dirname $0`
$LOCAL_PYTHON_PATH/sphinx-intl create-transifexrc
#rm -R pot  # skip this line cause "already unused pot files will not removed" but we must keep these files to avoid commit for only "POT-Creation-Time" line updated. see: https://github.com/sphinx-doc/sphinx/issues/3443
$LOCAL_PYTHON_PATH/sphinx-build -T -b gettext ../pyvista/docs pot
$LOCAL_PYTHON_PATH/sphinx-intl update-txconfig-resources -p pot -d .
cat .tx/config
$LOCAL_PYTHON_PATH/tx push -s --skip
rm -Rf ja
$LOCAL_PYTHON_PATH/tx pull -l ja
git checkout .tx/config
