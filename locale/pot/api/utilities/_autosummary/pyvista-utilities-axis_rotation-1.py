# Rotate a set of points by 90 degrees about the x-axis in-place.
#
import numpy as np
import pyvista
from pyvista import examples
points = examples.load_airplane().points
points_orig = points.copy()
pyvista.axis_rotation(points, 90, axis='x', deg=True, inplace=True)
assert np.all(np.isclose(points[:, 0], points_orig[:, 0]))
assert np.all(np.isclose(points[:, 1], -points_orig[:, 2]))
assert np.all(np.isclose(points[:, 2], points_orig[:, 1]))
