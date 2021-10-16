from pyvista import examples
grid = examples.load_explicit_structured()  # doctest:+SKIP
grid.plot(color='w', show_edges=True, show_bounds=True)  # doctest:+SKIP
#
grid.hide_cells(range(80, 120))  # doctest:+SKIP
grid.plot(color='w', show_edges=True, show_bounds=True)  # doctest:+SKIP
#
grid = grid.cast_to_unstructured_grid()  # doctest:+SKIP
grid.plot(color='w', show_edges=True, show_bounds=True)  # doctest:+SKIP
#
grid = grid.cast_to_explicit_structured_grid()  # doctest:+SKIP
grid.plot(color='w', show_edges=True, show_bounds=True)  # doctest:+SKIP
