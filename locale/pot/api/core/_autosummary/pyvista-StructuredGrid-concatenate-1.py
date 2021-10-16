# Split a grid in half and join them.
#
import numpy as np
import pyvista
from pyvista import examples
grid = examples.load_structured()
voi_1 = grid.extract_subset([0, 80, 0, 40, 0, 1], boundary=True)
voi_2 = grid.extract_subset([0, 80, 40, 80, 0, 1], boundary=True)
joined = voi_1.concatenate(voi_2, axis=1)
f'{grid.dimensions} same as {joined.dimensions}'
# Expected:
## '(80, 80, 1) same as (80, 80, 1)'
