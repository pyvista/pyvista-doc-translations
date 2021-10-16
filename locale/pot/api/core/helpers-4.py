# This example plots two line segments at right angles to each other.
#
import pyvista
import numpy as np
points = np.array([[0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 1, 0]])
lines = pyvista.lines_from_points(points)
lines.plot()
