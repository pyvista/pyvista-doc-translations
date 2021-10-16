# First, generate 30 points on circle and plot them.
#
import pyvista
points = pyvista.Polygon(n_sides=30).points
circle = pyvista.PolyData(points)
circle.plot(show_edges=True, point_size=15)
#
# Use :func:`delaunay_2d` to fill the interior of the circle.
#
filled_circle = circle.delaunay_2d()
filled_circle.plot(show_edges=True, line_width=5)
