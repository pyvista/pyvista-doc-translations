from pyvista import examples
grid = examples.load_explicit_structured()  # doctest:+SKIP
grid.compute_connections()  # doctest:+SKIP
grid.plot(show_edges=True)  # doctest:+SKIP
