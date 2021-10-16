# Add a floor below a sphere and plot it.
#
import pyvista
pl = pyvista.Plotter()
actor = pl.add_mesh(pyvista.Sphere())
actor = pl.add_floor()
pl.show()
