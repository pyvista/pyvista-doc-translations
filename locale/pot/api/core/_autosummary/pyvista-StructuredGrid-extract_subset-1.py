# Split a grid in half.
#
import numpy as np
import pyvista
from pyvista import examples
grid = examples.load_structured()
voi_1 = grid.extract_subset([0, 80, 0, 40, 0, 1], boundary=True)
voi_2 = grid.extract_subset([0, 80, 40, 80, 0, 1], boundary=True)
#
# For fun, add the two grids back together and show they are
# identical to the original grid.
#
joined = voi_1.concatenate(voi_2, axis=1)
assert np.allclose(grid.points, joined.points)
