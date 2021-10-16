import pyvista
pointa = [1.0, 0.0, 0.0]
pointb = [1.0, 1.0, 0.0]
pointc = [0.0, 1.0, 0.0]
pointd = [0.0, 0.0, 0.0]
rectangle = pyvista.Rectangle([pointa, pointb, pointc, pointd])
rectangle.plot(show_edges=True, line_width=5)
