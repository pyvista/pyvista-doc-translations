# Get the length of the bounding box of a cube.  This should
# match ``3**(1/2)`` since it is the diagonal of a cube that is
# ``1 x 1 x 1``.
#
import pyvista
mesh = pyvista.Cube()
mesh.length
# Expected:
## 1.7320508075688772
