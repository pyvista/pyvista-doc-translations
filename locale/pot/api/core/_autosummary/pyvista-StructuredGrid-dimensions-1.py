import pyvista
import numpy as np
xrng = np.arange(-10, 10, 1)
yrng = np.arange(-10, 10, 2)
zrng = np.arange(-10, 10, 5)
x, y, z = np.meshgrid(xrng, yrng, zrng)
grid = pyvista.StructuredGrid(x, y, z)
grid.dimensions
# Expected:
## (10, 20, 4)
