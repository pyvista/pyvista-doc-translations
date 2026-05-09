"""Inject the atsphinx.mini18n configuration into pyvista's conf.py.

The core pyvista docs build no longer pulls in ``atsphinx-mini18n`` (see
pyvista/pyvista#8626). The translated-docs pipeline uses this script to
re-enable mini18n by appending an overlay block to a checked-out copy of
``doc/source/conf.py`` before running ``sphinx-build``.

Idempotent: running twice on the same file is a no-op.
"""

import argparse
from pathlib import Path
from textwrap import dedent

OVERLAY_MARKER = '# >>> pyvista-doc-translations i18n overlay >>>'
OVERLAY_END_MARKER = '# <<< pyvista-doc-translations i18n overlay <<<'


def build_overlay(locale_dir: str) -> str:
    return dedent(
        f"""
        {OVERLAY_MARKER}
        # Injected by pyvista-doc-translations to enable atsphinx.mini18n for
        # the translated documentation build. The core pyvista docs build does
        # not include this extension.
        from atsphinx.mini18n import get_template_dir as _pdt_get_template_dir

        extensions = list(extensions) + ['atsphinx.mini18n']
        templates_path = list(templates_path) + [_pdt_get_template_dir()]
        locale_dirs = [r'{locale_dir}']
        mini18n_default_language = language
        mini18n_support_languages = ['en', 'ja']
        html_sidebars = {{
            '**': [
                'navbar-logo.html',
                'icon-links.html',
                'mini18n/snippets/select-lang.html',
                'search-button-field.html',
                'sbt-sidebar-nav.html',
            ],
        }}
        {OVERLAY_END_MARKER}
        """
    ).strip()


def apply_overlay(conf_path: Path, locale_dir: str) -> bool:
    text = conf_path.read_text(encoding='utf-8')
    if OVERLAY_MARKER in text:
        return False
    overlay = build_overlay(locale_dir)
    new_text = text.rstrip() + '\n\n\n' + overlay + '\n'
    conf_path.write_text(new_text, encoding='utf-8')
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '--conf',
        required=True,
        type=Path,
        help="Path to pyvista's doc/source/conf.py",
    )
    parser.add_argument(
        '--locale-dir',
        required=True,
        help='Absolute path to the translations locale directory',
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.conf.is_file():
        msg = f'conf.py not found at {args.conf}'
        raise SystemExit(msg)
    if not Path(args.locale_dir).is_dir():
        msg = f'locale dir not found at {args.locale_dir}'
        raise SystemExit(msg)
    changed = apply_overlay(args.conf, args.locale_dir)
    if changed:
        print(f'Applied i18n overlay to {args.conf}')
    else:
        print(f'i18n overlay already present in {args.conf}; skipping')


if __name__ == '__main__':
    main()
