# Translate a mesh by ``(50, 100, 200)``.
#
import numpy as np
from pyvista import examples
mesh = examples.load_airplane()
#
# Here a 4x4 :class:`numpy.ndarray` is used, but
# ``vtk.vtkMatrix4x4`` and ``vtk.vtkTransform`` are also
# accepted.
#
transform_matrix = np.array([[1, 0, 0, 50],
                             [0, 1, 0, 100],
                             [0, 0, 1, 200],
                             [0, 0, 0, 1]])
transformed = mesh.transform(transform_matrix)
transformed.plot(show_edges=True)
