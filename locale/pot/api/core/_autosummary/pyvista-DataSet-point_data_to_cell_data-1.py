# Color cells by their z coordinates.  First, create point
# scalars based on z-coordinates of a sample sphere mesh.  Then
# convert this point data to cell data.  Use a low resolution
# sphere for emphasis of cell valued data.
#
# First, plot these values as point values to show the
# difference between point and cell data.
#
import pyvista
sphere = pyvista.Sphere(theta_resolution=10, phi_resolution=10)
sphere['Z Coordinates'] = sphere.points[:, 2]
sphere.plot()
#
# Now, convert these values to cell data and then plot it.
#
import pyvista
sphere = pyvista.Sphere(theta_resolution=10, phi_resolution=10)
sphere['Z Coordinates'] = sphere.points[:, 2]
sphere = sphere.point_data_to_cell_data()
sphere.plot()
