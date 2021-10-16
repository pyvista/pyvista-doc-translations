# Create a light with a transformation matrix that corresponds
# to a 90-degree rotation around the z axis and a shift by (0,
# 0, -1), and check that the light's focal point transforms as
# expected.
#
import numpy as np
import pyvista as pv
light = pv.Light(focal_point=(1, 0, 3))
trans = np.zeros((4, 4))
trans[:-1, :-1] = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
trans[:-1, -1] = [0, 0, -1]
light.transform_matrix = trans
light.focal_point
# Expected:
## (1.0, 0.0, 3.0)
light.world_focal_point
# Expected:
## (0.0, 1.0, 2.0)
