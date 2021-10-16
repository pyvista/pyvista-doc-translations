import pyvista
from pyvista import examples
import vtk
#
# Create an empty grid
#
grid = pyvista.UnstructuredGrid()
#
# Copy a vtkUnstructuredGrid
#
vtkgrid = vtk.vtkUnstructuredGrid()
grid = pyvista.UnstructuredGrid(vtkgrid)  # Initialize from a vtkUnstructuredGrid
#
#
#
# From a string filename
#
grid = pyvista.UnstructuredGrid(examples.hexbeamfile)
