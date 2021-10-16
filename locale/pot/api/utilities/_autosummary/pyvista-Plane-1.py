# Create a default plane.
#
import pyvista
mesh = pyvista.Plane()
mesh.point_data.clear()
mesh.plot(show_edges=True)
