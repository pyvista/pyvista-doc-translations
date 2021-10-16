# Add point arrays to a mesh and list the available ``point_data``.
#
import pyvista
import numpy as np
mesh = pyvista.Cube()
mesh.clear_data()
mesh.point_data['my_array'] = np.random.random(mesh.n_points)
mesh.point_data['my_other_array'] = np.arange(mesh.n_points)
mesh.point_data
# Expected:
## pyvista DataSetAttributes
## Association     : POINT
## Active Scalars  : my_other_array
## Active Vectors  : None
## Active Texture  : None
## Active Normals  : None
## Contains arrays :
##     my_array                float64  (8,)
##     my_other_array          int64    (8,)                 SCALARS
#
# Access an array from ``point_data``.
#
mesh.point_data['my_other_array']
# Expected:
## pyvista_ndarray([0, 1, 2, 3, 4, 5, 6, 7])
#
# Or access it directly from the mesh.
#
mesh['my_array'].shape
# Expected:
## (8,)
