# Find nearest cell to a point on a sphere, centered on the
# origin.
#
import pyvista
mesh = pyvista.Sphere()
index = mesh.find_closest_cell([0, 0, 0.5])
index
# Expected:
## 30
#
# Find the nearest cells to several random points that
# are centered on the origin.
#
import numpy as np
points = 2 * np.random.random((5000, 3)) - 1
indices = mesh.find_closest_cell(points)
indices.shape
# Expected:
## (5000,)
#
# The average position of all the randomly found cell centers should
# be reasonably close to the origin.
#
cell_center_mesh = mesh.cell_centers()
avg_pos = cell_center_mesh.points[indices, :].mean(axis=0)
np.linalg.norm(avg_pos) < 0.02
# Expected:
## True
