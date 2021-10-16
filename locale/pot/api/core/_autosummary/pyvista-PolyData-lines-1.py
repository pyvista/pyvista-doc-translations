# Return the lines from a spline.
#
import pyvista
import numpy as np
points = np.random.random((3, 3))
spline = pyvista.Spline(points, 10)
spline.lines
# Expected:
## array([10,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9])
