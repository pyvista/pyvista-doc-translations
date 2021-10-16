# Create a light positioned at ``(10, 10, 10)`` after
# initialization, and note how the position is unaffected by a
# non-trivial transform matrix.
#
import numpy as np
import pyvista as pv
light = pv.Light()
light.position = (10, 10, 10)
light.transform_matrix = np.arange(4 * 4).reshape(4, 4)
light.position
# Expected:
## (10.0, 10.0, 10.0)
