from pyvista import examples
grid = examples.load_explicit_structured()  # doctest:+SKIP
grid.cell_id((3, 4, 0))  # doctest:+SKIP
# Expected:
## 19
#
coords = [(3, 4, 0),
          (3, 2, 1),
          (1, 0, 2),
          (2, 3, 2)]
grid.cell_id(coords)  # doctest:+SKIP
# Expected:
## array([19, 31, 41, 54])
