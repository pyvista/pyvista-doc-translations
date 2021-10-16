# Add cell arrays to a mesh and list the available ``cell_data``.
#
import pyvista
import numpy as np
mesh = pyvista.Cube()
mesh.clear_data()
mesh.cell_data['my_array'] = np.random.random(mesh.n_cells)
mesh.cell_data['my_other_array'] = np.arange(mesh.n_cells)
mesh.cell_data
# Expected:
## pyvista DataSetAttributes
## Association     : CELL
## Active Scalars  : my_other_array
## Active Vectors  : None
## Active Texture  : None
## Active Normals  : None
## Contains arrays :
##     my_array                float64  (6,)
##     my_other_array          int64    (6,)                 SCALARS
#
# Access an array from ``cell_data``.
#
mesh.cell_data['my_other_array']
# Expected:
## pyvista_ndarray([0, 1, 2, 3, 4, 5])
#
# Or access it directly from the mesh.
#
mesh['my_array'].shape
# Expected:
## (6,)
