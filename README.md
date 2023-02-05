# translated docs for pyvista official document

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)

This is a project to provide pyvista official documentation with and multiple languages.
This repository is inspired by [sphinx-doc/sphinx-doc-translations](https://github.com/sphinx-doc/sphinx-doc-translations.git).

## URLs

* Documentation pages for each languages:

  * https://pyvista.github.io/pyvista-docs-dev-ja/


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

1. update po files

1. commit them
