from pyvista import examples
grid = examples.load_explicit_structured()
_ = grid.hide_cells(range(80, 120))
grid.plot(color='w', show_edges=True, show_bounds=True)
