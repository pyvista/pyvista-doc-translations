# Return the number of open edges on a sphere.
#
import pyvista
sphere = pyvista.Sphere()
sphere.n_open_edges
# Expected:
## 0
#
# Return the number of open edges on a plane.
#
plane = pyvista.Plane(i_resolution=1, j_resolution=1)
plane.n_open_edges
# Expected:
## 4
