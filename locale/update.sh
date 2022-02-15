#!/bin/sh
# update transifex pot and local po files

set -ex

# required environment variables
# SPHINXINTL_TRANSIFEX_USERNAME=tkoyama010
# SPHINXINTL_TRANSIFEX_PROJECT_NAME=pyvista-doc
LOCAL_PYTHON_PATH="../.venv/bin"

# pull po files from transifex
cd `dirname $0`
source $LOCAL_PYTHON_PATH/activate
sphinx-intl create-transifexrc
#rm -R pot  # skip this line cause "already unused pot files will not removed" but we must keep these files to avoid commit for only "POT-Creation-Time" line updated. see: https://github.com/sphinx-doc/sphinx/issues/3443
sphinx-build -T -b gettext ../pyvista/doc pot || true  # will fail on VTK9
sphinx-build -T -b gettext ../pyvista/doc pot || true  # need it again due to all our docstring examples
sphinx-build -T -b gettext ../pyvista/doc pot
sphinx-intl update-txconfig-resources -p pot -d .
cat .tx/config
tx push -s --skip
rm -Rf ja zh_CN zh_TW jv pl_PL
$LOCAL_PYTHON_PATH/tx pull -l ja,zh_CN,zh_TW,jv,pl_PL
git checkout .tx/config
deactivate
