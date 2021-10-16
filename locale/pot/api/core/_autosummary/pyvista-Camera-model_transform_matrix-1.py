import pyvista
import numpy as np
pl = pyvista.Plotter()
pl.camera.model_transform_matrix
# Expected:
## array([[1., 0., 0., 0.],
##        [0., 1., 0., 0.],
##        [0., 0., 1., 0.],
##        [0., 0., 0., 1.]])
pl.camera.model_transform_matrix = np.array([[1., 0., 0., 0.],
                                             [0., 1., 0., 0.],
                                             [0., 0., 1., 0.],
                                             [0., 0., 0., 0.5]])
