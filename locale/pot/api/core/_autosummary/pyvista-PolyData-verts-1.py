# Create a point cloud polydata and return the vertex cells.
#
import pyvista
import numpy as np
points = np.random.random((5, 3))
pdata = pyvista.PolyData(points)
pdata.verts
# Expected:
## array([1, 0, 1, 1, 1, 2, 1, 3, 1, 4])
#
# Set vertex cells.  Note how the mesh plots both the surface
# mesh and the additional vertices in a single plot.
#
mesh = pyvista.Plane(i_resolution=3, j_resolution=3)
mesh.verts = np.vstack((np.ones(mesh.n_points, dtype=np.int64),
                        np.arange(mesh.n_points))).T
mesh.plot(color='tan', render_points_as_spheres=True, point_size=60)
