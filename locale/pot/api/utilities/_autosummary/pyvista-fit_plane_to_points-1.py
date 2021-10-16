# Fit a plane to a random point cloud.
#
import pyvista
import numpy as np
cloud = np.random.random((10, 3))
cloud[:, 2] *= 0.1
plane, center, normal = pyvista.fit_plane_to_points(cloud, return_meta=True)
#
# Plot the fitted plane.
#
pl = pyvista.Plotter()
_ = pl.add_mesh(plane, color='tan', style='wireframe', line_width=4)
_ = pl.add_points(cloud, render_points_as_spheres=True, 
                  color='r', point_size=30)
pl.show()
