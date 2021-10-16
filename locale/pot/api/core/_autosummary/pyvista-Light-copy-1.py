# Create a light and check that it shares a transformation
# matrix with its shallow copy.
#
import pyvista as pv
light = pv.Light()
light.transform_matrix = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], 
                          [0, 0, 0, 1]]
shallow_copied = light.copy(deep=False)
shallow_copied == light
# Expected:
## True
shallow_copied.transform_matrix is light.transform_matrix
# Expected:
## True
