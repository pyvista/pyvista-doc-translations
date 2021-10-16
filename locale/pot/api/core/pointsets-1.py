# Load module and example file
import pyvista as pv
from pyvista import examples
import numpy as np

# Load example beam grid
grid = pv.UnstructuredGrid(examples.hexbeamfile)

# Create fictitious displacements as a function of Z location
d = np.zeros_like(grid.points)
d[:, 1] = grid.points[:, 2]**3/250

# Displace original grid
grid.points += d