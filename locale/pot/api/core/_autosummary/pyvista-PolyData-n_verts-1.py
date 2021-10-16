# Create a simple mesh containing just two points and return the
# number of vertices.
#
import pyvista
mesh = pyvista.PolyData([[1, 0, 0], [1, 1, 1]])
mesh.n_verts
# Expected:
## 2
