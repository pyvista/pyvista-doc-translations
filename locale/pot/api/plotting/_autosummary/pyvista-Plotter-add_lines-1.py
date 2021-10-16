import numpy as np
import pyvista
pl = pyvista.Plotter()       
points = np.array([[0, 1, 0], [1, 0, 0], [1, 1, 0], [2, 0, 0]])
actor = pl.add_lines(points, color='yellow', width=3)
pl.camera_position = 'xy'
pl.show()
