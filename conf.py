# basedir is set by <lang>/conf.py
"""
Use "-D language=<LANG>" option to build a localized pyvista document.
For example::

    sphinx-build -D language=ja -b html . _build/html
This conf.py do:
- Specify `locale_dirs` and `gettext_compact`.
- Overrides source directory as 'pyvista/docs`.
"""
import os
import shutil
import sys

from sphinx.util.pycompat import execfile_

shutil.rmtree("pyvista/docs/examples", ignore_errors=True)
shutil.copytree("locale/examples", "pyvista/docs/examples")
shutil.rmtree("pyvista/docs/images/auto-generated", ignore_errors=True)
shutil.copytree("locale/images/auto-generated", "pyvista/docs/images/auto-generated")
