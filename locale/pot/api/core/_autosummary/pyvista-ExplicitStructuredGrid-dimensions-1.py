from pyvista import examples
grid = examples.load_explicit_structured()  # doctest:+SKIP
grid.dimensions  # doctest:+SKIP
# Expected:
## array([5, 6, 7])
