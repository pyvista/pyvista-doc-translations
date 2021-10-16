import pyvista
import numpy as np
points = np.random.random((10, 3))
vpoints = pyvista.vtk_points(points)
vpoints  # doctest:+SKIP
# Expected:
## (vtkmodules.vtkCommonCore.vtkPoints)0x7f0c2e26af40
