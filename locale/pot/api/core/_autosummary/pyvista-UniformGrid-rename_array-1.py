# Create a cube, assign a point array to the mesh named
# ``'my_array'``, and rename it to ``'my_renamed_array'``.
#
import pyvista
import numpy as np
cube = pyvista.Cube()
cube['my_array'] = range(cube.n_points)
cube.rename_array('my_array', 'my_renamed_array')
cube['my_renamed_array']
# Expected:
## array([0, 1, 2, 3, 4, 5, 6, 7])
