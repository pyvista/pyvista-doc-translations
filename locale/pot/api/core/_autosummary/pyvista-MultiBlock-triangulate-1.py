# Generate a mesh with quadrilateral faces.
#
import pyvista
plane = pyvista.Plane()
plane.point_data.clear()
plane.plot(show_edges=True, line_width=5)
#
# Convert it to an all triangle mesh.
#
mesh = plane.triangulate()
mesh.plot(show_edges=True, line_width=5)
