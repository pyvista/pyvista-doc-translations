# Create a plotter without any lights and then enable the
# default light kit.
#
import pyvista
pl = pyvista.Plotter(lighting=None)
pl.enable_lightkit()
actor = pl.add_mesh(pyvista.Cube(), show_edges=True)
pl.show()
