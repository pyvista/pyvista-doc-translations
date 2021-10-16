# Add two meshes to a plotter and then remove the sphere actor.
#
import pyvista
mesh = pyvista.Cube()
pl = pyvista.Plotter()
cube_actor = pl.add_mesh(pyvista.Cube(), show_edges=True)
sphere_actor = pl.add_mesh(pyvista.Sphere(), show_edges=True)
_ = pl.remove_actor(cube_actor)
pl.show()
