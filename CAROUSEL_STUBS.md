# Dataset Carousel Stub Generation

## Problem

The PyVista documentation includes a dataset gallery with carousel files that are auto-generated during the documentation build process by `pyvista/doc/source/make_tables.py`. These files are referenced in `pyvista/doc/source/api/examples/dataset_gallery.rst`.

For translation builds, where the full PyVista build with all dependencies is not run, these carousel files don't exist, causing the Sphinx build to fail with CRITICAL errors about missing include files.

## Solution

The `generate_carousel_stubs.py` script creates minimal placeholder files for all the carousel files. These stubs:

1. Allow the documentation build to succeed without errors
2. Provide a helpful message directing users to the full PyVista documentation for the complete dataset gallery
3. Are generated in two locations to work with different build configurations:
   - `pyvista/doc/source/api/examples/dataset-gallery/` - for building PyVista docs directly
   - `api/examples/dataset-gallery/` - for translation builds from the repository root

## Usage

### ReadTheDocs Build

The `.readthedocs.yaml` configuration runs the stub generation script automatically before the Sphinx build:

```yaml
build:
  jobs:
    pre_build:
      - python generate_carousel_stubs.py
```

### GitHub Actions

The GitHub Actions workflow in `.github/workflows/main.yml` also runs the stub generation as a fallback if the full PyVista documentation build fails:

```yaml
make -C doc html SPHINXOPTS="-w build_errors.txt -N" || {
  echo "WARNING: PyVista doc build failed, using stub carousel files"
  cd ..
  python generate_carousel_stubs.py
  cd pyvista
}
python generate_carousel_stubs.py  # Ensure stubs exist
```

### Manual Generation

To manually generate the stub files:

```bash
python generate_carousel_stubs.py
```

## Files Generated

The script generates 23 carousel files:

- `all_datasets_carousel.rst`
- `builtin_carousel.rst`
- `downloads_carousel.rst`
- `planets_carousel.rst`
- `pointset_carousel.rst`
- `polydata_carousel.rst`
- `unstructuredgrid_carousel.rst`
- `structuredgrid_carousel.rst`
- `explicitstructuredgrid_carousel.rst`
- `pointcloud_carousel.rst`
- `surfacemesh_carousel.rst`
- `rectilineargrid_carousel.rst`
- `imagedata_carousel.rst`
- `imagedata_3d_carousel.rst`
- `imagedata_2d_carousel.rst`
- `texture_carousel.rst`
- `cubemap_carousel.rst`
- `multiblock_carousel.rst`
- `multiblock_homo_carousel.rst`
- `multiblock_hetero_carousel.rst`
- `multiblock_single_carousel.rst`
- `misc_carousel.rst`
- `medical_carousel.rst`

## Maintenance

If new carousel files are added to the PyVista documentation, they should be added to the `CAROUSEL_FILES` list in `generate_carousel_stubs.py`.
