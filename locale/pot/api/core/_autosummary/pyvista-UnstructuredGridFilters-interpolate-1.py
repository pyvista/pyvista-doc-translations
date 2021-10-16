# Interpolate the values of 5 points onto a sample plane.
#
import pyvista
import numpy as np
np.random.seed(7)
point_cloud = np.random.random((5, 3))
point_cloud[:, 2] = 0
point_cloud -= point_cloud.mean(0)
pdata = pyvista.PolyData(point_cloud)
pdata['values'] = np.random.random(5)
plane = pyvista.Plane()
plane.clear_data()
plane = plane.interpolate(pdata, sharpness=3)
pl = pyvista.Plotter()
_ = pl.add_mesh(pdata, render_points_as_spheres=True, point_size=50)
_ = pl.add_mesh(plane, style='wireframe', line_width=5)
pl.show()
