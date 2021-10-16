import pyvista
import vtk
import numpy as np
#
# Create empty grid
#
grid = pyvista.StructuredGrid()
#
# Initialize from a vtk.vtkStructuredGrid object
#
vtkgrid = vtk.vtkStructuredGrid()
grid = pyvista.StructuredGrid(vtkgrid)
#
# Create from NumPy arrays
#
xrng = np.arange(-10, 10, 2)
yrng = np.arange(-10, 10, 2)
zrng = np.arange(-10, 10, 2)
x, y, z = np.meshgrid(xrng, yrng, zrng)
grid = pyvista.StructuredGrid(x, y, z)
