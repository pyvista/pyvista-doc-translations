from pyvista import examples
mesh = examples.load_airplane()
mesh = mesh.reflect((0, 0, 1), point=(0, 0, -100))
mesh.plot(show_edges=True)
