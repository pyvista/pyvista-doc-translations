import pyvista
import vtk
import numpy as np
#
# Create an empty grid
#
grid = pyvista.RectilinearGrid()
#
# Initialize from a vtk.vtkRectilinearGrid object
#
vtkgrid = vtk.vtkRectilinearGrid()
grid = pyvista.RectilinearGrid(vtkgrid)
#
# Create from NumPy arrays
#
xrng = np.arange(-10, 10, 2)
yrng = np.arange(-10, 10, 5)
zrng = np.arange(-10, 10, 1)
grid = pyvista.RectilinearGrid(xrng, yrng, zrng)
