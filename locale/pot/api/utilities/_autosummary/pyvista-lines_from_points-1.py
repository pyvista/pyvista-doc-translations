import numpy as np
import pyvista
points = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0]])
poly = pyvista.lines_from_points(points)
poly.plot(line_width=5)
