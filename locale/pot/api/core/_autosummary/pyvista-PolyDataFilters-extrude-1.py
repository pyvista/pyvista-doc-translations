# Extrude a half circle arc.
#
import pyvista
arc = pyvista.CircularArc([-1, 0, 0], [1, 0, 0], [0, 0, 0])
mesh = arc.extrude([0, 0, 1])
mesh.plot(color='tan')
#
# Extrude and cap an 8 sided polygon.
#
poly = pyvista.Polygon(n_sides=8)
mesh = poly.extrude((0, 0, 1.5), capping=True)
mesh.plot(line_width=5, show_edges=True)
