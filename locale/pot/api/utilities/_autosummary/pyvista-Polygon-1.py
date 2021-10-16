# Create an 8 sided polygon.
#
import pyvista
mesh = pyvista.Polygon(n_sides=8)
mesh.plot(show_edges=True, line_width=5)
