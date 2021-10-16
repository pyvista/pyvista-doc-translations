import pyvista as pv
from pyvista import examples
grid = examples.load_explicit_structured()  # doctest:+SKIP
grid.hide_cells(range(80, 120))  # doctest:+SKIP
grid.save('grid.vtu')  # doctest:+SKIP
#
grid = pv.ExplicitStructuredGrid('grid.vtu')  # doctest:+SKIP
grid.plot(color='w', show_edges=True, show_bounds=True)  # doctest:+SKIP
#
grid.show_cells()  # doctest:+SKIP
grid.plot(color='w', show_edges=True, show_bounds=True)  # doctest:+SKIP
