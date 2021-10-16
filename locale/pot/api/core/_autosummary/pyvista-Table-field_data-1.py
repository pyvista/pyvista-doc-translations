# Add field data to a PolyData dataset and then return it.
#
import pyvista
import numpy as np
mesh = pyvista.Sphere()
mesh.field_data['my-field-data'] = np.arange(10)
mesh.field_data['my-field-data']
# Expected:
## pyvista_ndarray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
