# Add a numpy array of points to a mesh.
#
import numpy as np
import pyvista
points = np.random.random((10, 3))
pl = pyvista.Plotter()
actor = pl.add_points(points, render_points_as_spheres=True, 
                      point_size=100.0)
pl.show()
