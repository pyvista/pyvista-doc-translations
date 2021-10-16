import pyvista
pointa = [0, 0, 0]
pointb = [1, 0, 0]
pointc = [0.5, 0.707, 0]
triangle = pyvista.Triangle([pointa, pointb, pointc])
triangle.plot(show_edges=True, line_width=5)
