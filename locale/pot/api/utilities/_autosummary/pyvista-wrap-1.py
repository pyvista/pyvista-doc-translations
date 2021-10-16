# Wrap a numpy array representing a random point cloud.
#
import numpy as np
import pyvista
points = np.random.random((10, 3))
cloud = pyvista.wrap(points)
cloud  # doctest:+SKIP
# Expected:
## PolyData (0x7fc52db83d70)
##   N Cells:  10
##   N Points: 10
##   X Bounds: 1.123e-01, 7.457e-01
##   Y Bounds: 1.009e-01, 9.877e-01
##   Z Bounds: 2.346e-03, 9.640e-01
##   N Arrays: 0
#
# Wrap a Trimesh object.
#
import trimesh
import pyvista
points = [[0, 0, 0], [0, 0, 1], [0, 1, 0]]
faces = [[0, 1, 2]]
tmesh = trimesh.Trimesh(points, faces=faces, process=False)
mesh = pyvista.wrap(tmesh)
mesh  # doctest:+SKIP
# Expected:
## PolyData (0x7fc55ff27ad0)
##   N Cells:  1
##   N Points: 3
##   X Bounds: 0.000e+00, 0.000e+00
##   Y Bounds: 0.000e+00, 1.000e+00
##   Z Bounds: 0.000e+00, 1.000e+00
##   N Arrays: 0
#
# Wrap a VTK object.
#
import pyvista
import vtk
points = vtk.vtkPoints()
p = [1.0, 2.0, 3.0]
vertices = vtk.vtkCellArray()
pid = points.InsertNextPoint(p)
_ = vertices.InsertNextCell(1)
_ = vertices.InsertCellPoint(pid)
point = vtk.vtkPolyData()
_ = point.SetPoints(points)
_ = point.SetVerts(vertices)
mesh = pyvista.wrap(point)
mesh  # doctest:+SKIP
# Expected:
## PolyData (0x7fc55ff27ad0)
##   N Cells:  1
##   N Points: 3
##   X Bounds: 0.000e+00, 0.000e+00
##   Y Bounds: 0.000e+00, 1.000e+00
##   Z Bounds: 0.000e+00, 1.000e+00
##   N Arrays: 0
