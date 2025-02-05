#!/bin/sh
# update transifex pot and local po files

set -ex

# required environment variables
# SPHINXINTL_TRANSIFEX_USERNAME=tkoyama010
# SPHINXINTL_TRANSIFEX_PROJECT_NAME=pyvista-doc

# pull po files from transifex
cd `dirname $0`
#rm -R pot  # skip this line cause "already unused pot files will not removed" but we must keep these files to avoid commit for only "POT-Creation-Time" line updated. see: https://github.com/sphinx-doc/sphinx/issues/3443
sphinx-build -T -b gettext ../pyvista/doc/source pot
sphinx-intl update-txconfig-resources -p pot -d .
cat .tx/config
tx push -s --skip
rm -Rf ja zh zh_CN zh_Hans zh_TW en_CA en_US de_DE jv nb pl pl_PL ru es uk fa ko_KR
tx pull --silent -f -l ja,zh_CN,zh_Hans,zh_TW,en_CA,en_US,de_DE,jv,nb,pl,pl_PL,ru,es,uk,fa,ko_KR
git checkout .tx/config
