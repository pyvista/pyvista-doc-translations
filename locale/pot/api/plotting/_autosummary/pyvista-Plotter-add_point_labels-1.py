import numpy as np
import pyvista
pl = pyvista.Plotter()
points = np.array([[0, 0, 0],
                   [1, 1, 0],
                   [2, 0, 0]])
labels = ['Point A', 'Point B', 'Point C']
actor = pl.add_point_labels(points, labels, italic=True, font_size=20,
                            point_color='red', point_size=20, render_points_as_spheres=True,
                            always_visible=True, shadow=True)
pl.camera_position = 'xy'
pl.show()
