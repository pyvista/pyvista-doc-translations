# translated docs for pyvista official document

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/pyvista/pyvista-doc-translations/main.svg)](https://results.pre-commit.ci/latest/github/pyvista/pyvista-doc-translations/main)

This is a project to provide pyvista official documentation in multiple languages.
This repository is inspired by [sphinx-doc/sphinx-doc-translations](https://github.com/sphinx-doc/sphinx-doc-translations.git).

## URLs

- Documentation pages for each languages:
  - 日本語: https://pyvista.github.io/pyvista-docs-dev-ja/

## Build pipeline

The translated documentation is built by a dedicated GitHub Actions workflow
in this repo (`.github/workflows/build-i18n-docs.yml`). It used to live inside
`pyvista/pyvista`'s docs workflow, but was extracted in
[pyvista/pyvista#8626](https://github.com/pyvista/pyvista/issues/8626) so that:

- the multi-hour translated build no longer gates core docs releases;
- i18n-only build errors surface in their own pipeline instead of breaking the
  English release deploy;
- translators can request a build at any time without waiting on a PyVista
  release.

### Triggers

- **`workflow_dispatch`** — manual run. Optional `pyvista_ref` input selects
  the pyvista tag/branch/sha to build against; defaults to the latest pyvista
  release tag.
- **`schedule`** — weekly preview build (Monday 06:00 UTC) against the latest
  pyvista release tag.
- **`repository_dispatch`** with event type `pyvista-release` — allows
  pyvista's release workflow to fan out a translated build, with the released
  tag in `client_payload.pyvista_ref`.

### How the build works

1. Checks out this repo (for `locale/`) and `pyvista/pyvista` at the requested
   ref into a sibling directory.
2. Installs pyvista's `docs` dependency group plus `atsphinx-mini18n` (the
   latter is intentionally not in pyvista's docs group anymore).
3. Runs `scripts/apply_i18n_overlay.py` to append a small overlay block to
   pyvista's `doc/source/conf.py`. The overlay re-enables `atsphinx.mini18n`,
   sets `locale_dirs` to this repo's `locale/`, and adds the language-selector
   sidebar entry. It is idempotent.
4. Runs `sphinx-build -M mini18n-html` to produce one HTML tree per supported
   language, and uploads the non-English subtrees as the `i18n-docs` artifact.

Production deployment of the artifact (e.g. to `docs.pyvista.org/ja/`) is
handled outside this workflow.

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
