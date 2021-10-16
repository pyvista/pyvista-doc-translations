# Create a mesh, compute the normals and set them active, and
# plot the active vectors.
#
import pyvista
mesh = pyvista.Cube()
mesh_w_normals = mesh.compute_normals()
mesh_w_normals.active_vectors_name = 'Normals'
arrows = mesh_w_normals.arrows
arrows.plot(show_scalar_bar=False)
