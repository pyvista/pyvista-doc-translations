# Create a light with a transformation matrix that corresponds to a
# 90-degree rotation around the z axis and a shift by (0, 0, -1), and
# check that the light's position transforms as expected.
#
import numpy as np
import pyvista as pv
light = pv.Light(position=(1, 0, 3))
trans = np.zeros((4, 4))
trans[:-1, :-1] = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
trans[:-1, -1] = [0, 0, -1]
light.transform_matrix = trans
light.position
# Expected:
## (1.0, 0.0, 3.0)
light.world_position
# Expected:
## (0.0, 1.0, 2.0)
