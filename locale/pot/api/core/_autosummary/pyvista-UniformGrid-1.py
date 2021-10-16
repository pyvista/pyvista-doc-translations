import pyvista
import vtk
import numpy as np
#
grid = pyvista.UniformGrid()
#
vtkgrid = vtk.vtkImageData()
grid = pyvista.UniformGrid(vtkgrid)
#
dims = (10, 10, 10)
grid = pyvista.UniformGrid(dims)
#
spacing = (2, 1, 5)
grid = pyvista.UniformGrid(dims, spacing)
#
origin = (10, 35, 50)
grid = pyvista.UniformGrid(dims, spacing, origin)
