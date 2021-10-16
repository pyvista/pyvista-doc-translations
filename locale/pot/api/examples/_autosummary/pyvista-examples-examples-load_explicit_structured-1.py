from pyvista import examples
grid = examples.load_explicit_structured()
grid.plot(show_edges=True)
