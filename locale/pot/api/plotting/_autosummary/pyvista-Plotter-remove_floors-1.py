# Add a floor below a sphere, remove it, and then plot it.
#
import pyvista
pl = pyvista.Plotter()
actor = pl.add_mesh(pyvista.Sphere())
actor = pl.add_floor()
pl.remove_floors()
pl.show()
