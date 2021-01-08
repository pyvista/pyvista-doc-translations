# pyvista-doc.org on the Read The Docs.
translated docs for pyvista official document

:us:

[![Documentation Status](https://readthedocs.org/projects/pyvista-doc/badge/?version=latest)](https://pyvista-doc.readthedocs.io/en/latest/?badge=latest)

:jp:

[![Documentation Status](https://readthedocs.org/projects/pyvista-doc-ja/badge/?version=latest)](https://pyvista-doc-ja.readthedocs.io/ja/latest/?badge=latest)

:cn:

[![Documentation Status](https://readthedocs.org/projects/pyvista-doc-zh-cn/badge/?version=latest)](https://pyvista-doc.readthedocs.io/zh_CN/latest/?badge=latest)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a project to provide pyvista official documentation with multiple versions and multiple languages on Read The Docs site.

Current procedure is bit tricky because Read The Docs doesn't have a way to specify options for sphinx-build command.
conf.py files for each languages have 'language' and 'locale_dirs' values without having full copy of conf.py of sphinx doc. If we want to specify conf.py file that is out of source directory, we will use '-c' option for sphinx-build command. Unfortunately Read the Docs can't. If there are any better way, please let me know.

## URLs

* RTD project pages for Sphinx:

  * https://readthedocs.org/projects/pyvista-doc/  (Master)
  * https://readthedocs.org/projects/pyvista-doc-ja/
  * https://readthedocs.org/projects/pyvista-doc-zh-cn/
  * https://readthedocs.org/projects/pyvista-doc-zh-tw/

* Documentation pages for each languages:

  * https://pyvista-doc.readthedocs.io/en/latest/
  * https://pyvista-doc.readthedocs.io/ja/latest/
  * https://pyvista-doc.readthedocs.io/zh_CN/latest/
  * https://pyvista-doc.readthedocs.io/zh_TW/latest/

## How to setup a translated documentation project on RTD

Detail is here: https://docs.readthedocs.org/en/latest/localization.html#project-with-multiple-translations

Points are:

* We must have RTD projects for each languages.
* Each projects must have correct Language setting on "Settings" page.
* Master project has connections to each translated projects on "translations settings" page.


## How to update po files

```
sh ./locale/update.sh
```

After that, you should commit updated po files.


## How to add a language

1. add language to locale/update.sh:

   ```
   - rm -R ja
   - tx pull -l ja
   + rm -R ja de
   + tx pull -l ja,de
   ```

2. update po files

3. commit them

4. add new project on Read The Docs like:

   https://readthedocs.org/projects/pyvista-doc-ja/

5. add translation project to parent project like:

   https://readthedocs.org/dashboard/pyvista-doc/translations/


## How to add a new version

1. add tag `1.7`

   ```
   git tag 1.7
   ```

2. replace old version `1_7` with `1_8` in:

   - release.sh
   - .travis.yml

3. commit it and push them:

   ```
   git add release.sh .travis.yml
   git commit -m "add new version: 1.8"
   git push --tags
   ```

4. enable version 1.7 on RTD:

   https://readthedocs.org/projects/pyvista-doc/versions/

