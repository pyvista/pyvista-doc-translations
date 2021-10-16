from pyvista import examples
grid = examples.load_explicit_structured()  # doctest:+SKIP
grid.hide_cells(range(80, 120))  # doctest:+SKIP
grid.bounds  # doctest:+SKIP
# Expected:
## [0.0, 80.0, 0.0, 50.0, 0.0, 6.0]
#
grid.visible_bounds  # doctest:+SKIP
# Expected:
## [0.0, 80.0, 0.0, 50.0, 0.0, 4.0]
