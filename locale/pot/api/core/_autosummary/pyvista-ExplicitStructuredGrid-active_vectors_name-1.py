# Create a mesh, compute the normals, set them as active, and
# return the name of the active vectors.
#
import pyvista
mesh = pyvista.Sphere()
mesh_w_normals = mesh.compute_normals()
mesh_w_normals.active_vectors_name = 'Normals'
mesh_w_normals.active_vectors_name
# Expected:
## 'Normals'
