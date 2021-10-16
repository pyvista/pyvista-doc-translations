from pyvista import examples
grid = examples.load_explicit_structured()
grid.plot(color='w', show_edges=True, show_bounds=True)
#
_ = grid.hide_cells(range(80, 120))
grid.plot(color='w', show_edges=True, show_bounds=True)
#
grid = grid.cast_to_unstructured_grid()
grid.plot(color='w', show_edges=True, show_bounds=True)
#
grid = grid.cast_to_explicit_structured_grid()
grid.plot(color='w', show_edges=True, show_bounds=True)
