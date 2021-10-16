# This example discretizes the unit square into a triangle mesh with
# nine vertices and eight faces.
#
import numpy as np
import pyvista
points = np.array([[0, 0, 0], [0.5, 0, 0], [1, 0, 0], [0, 0.5, 0],
                   [0.5, 0.5, 0], [1, 0.5, 0], [0, 1, 0], [0.5, 1, 0],
                   [1, 1, 0]])
faces = np.array([[0, 1, 4], [4, 7, 6], [2, 5, 4], [4, 5, 8],
                  [0, 4, 3], [3, 4, 6], [1, 2, 4], [4, 8, 7]])
tri_mesh = pyvista.make_tri_mesh(points, faces)
tri_mesh.plot(show_edges=True, line_width=5)
