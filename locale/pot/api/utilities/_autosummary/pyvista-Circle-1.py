import pyvista
radius = 0.5
circle = pyvista.Circle(radius)
circle.plot(show_edges=True, line_width=5)
