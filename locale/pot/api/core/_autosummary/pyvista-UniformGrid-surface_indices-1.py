# Return the first 10 surface indices of an UnstructuredGrid.
#
from pyvista import examples
grid = examples.load_hexbeam()
ind = grid.surface_indices()
ind[:10]  # doctest:+SKIP
# Expected:
## pyvista_ndarray([ 0,  2, 36, 27,  7,  8, 81,  1, 18,  4])
