# Find nearest cell to a point on a sphere
#
import pyvista
mesh = pyvista.Sphere()
index = mesh.find_closest_cell([0, 0, 0.5])
index
# Expected:
## 59
#
# Find the nearest cells to several random points.  Note that
# ``-1`` indicates that the locator was not able to find a
# reasonably close cell.
#
import numpy as np
points = np.random.random((1000, 3))
indices = mesh.find_closest_cell(points)
indices.shape
# Expected:
## (1000,)
