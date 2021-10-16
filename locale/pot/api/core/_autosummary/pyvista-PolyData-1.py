import vtk
import numpy as np
from pyvista import examples
import pyvista
#
# Create an empty mesh.
#
mesh = pyvista.PolyData()
#
# Initialize from a ``vtk.vtkPolyData`` object.
#
vtkobj = vtk.vtkPolyData()
mesh = pyvista.PolyData(vtkobj)
#
# Initialize from just vertices.
#
vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 0.5, 0], [0, 0.5, 0]])
mesh = pyvista.PolyData(vertices)
#
# Initialize from vertices and faces.
#
faces = np.hstack([[3, 0, 1, 2], [3, 0, 3, 2]])
mesh = pyvista.PolyData(vertices, faces)
#
# Initialize from vertices and lines.
#
lines = np.hstack([[2, 0, 1], [2, 1, 2]])
mesh = pyvista.PolyData(vertices, lines=lines)
#
# Initialize from a filename.
#
mesh = pyvista.PolyData(examples.antfile)
