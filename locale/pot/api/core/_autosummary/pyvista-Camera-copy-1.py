# Create a camera and check that it shares a transformation
# matrix with its shallow copy.
#
import pyvista as pv
import numpy as np
camera = pv.Camera()
camera.model_transform_matrix = np.array([[1., 0., 0., 0.],
                                          [0., 1., 0., 0.],
                                          [0., 0., 1., 0.],
                                          [0., 0., 0., 1.]])
copied_camera = camera.copy()
copied_camera == camera
# Expected:
## True
camera.model_transform_matrix = np.array([[1., 0., 0., 0.],
                                          [0., 1., 0., 0.],
                                          [0., 0., 1., 0.],
                                          [0., 0., 0., 0.5]])
copied_camera == camera
# Expected:
## False
