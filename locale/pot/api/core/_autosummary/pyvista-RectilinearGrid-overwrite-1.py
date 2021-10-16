# Create two meshes and overwrite ``mesh_a`` with ``mesh_b``.
# Show that ``mesh_a`` is equal to ``mesh_b``.
#
import pyvista
mesh_a = pyvista.Sphere()
mesh_b = pyvista.Cube()
mesh_a.overwrite(mesh_b)
mesh_a == mesh_b
# Expected:
## True
