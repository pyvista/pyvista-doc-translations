import pyvista as pv
from pyvista import examples
grid = examples.load_explicit_structured()  # doctest:+SKIP
cell = grid.extract_cells(31)  # doctest:+SKIP
ind = grid.neighbors(31)  # doctest:+SKIP
neighbors = grid.extract_cells(ind)  # doctest:+SKIP
plotter = pv.Plotter()
plotter.add_axes()  # doctest:+SKIP
plotter.add_mesh(cell, color='r', show_edges=True)  # doctest:+SKIP
plotter.add_mesh(neighbors, color='w', show_edges=True)  # doctest:+SKIP
plotter.show()  # doctest:+SKIP
