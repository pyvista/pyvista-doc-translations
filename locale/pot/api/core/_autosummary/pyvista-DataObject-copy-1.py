# Create and make a deep copy of a PolyData object.
#
import pyvista
mesh_a = pyvista.Sphere()
mesh_b = mesh_a.copy()
mesh_a == mesh_b
# Expected:
## True
