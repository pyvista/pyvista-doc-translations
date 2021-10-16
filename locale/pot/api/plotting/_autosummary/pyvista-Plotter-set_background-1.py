# Set the background color to black.
#
import pyvista
plotter = pyvista.Plotter()
plotter.set_background('black')
plotter.background_color
# Expected:
## (0.0, 0.0, 0.0)
#
# Set the background color at the bottom to black and white at
# the top.  Display a cone as well.
#
import pyvista
pl = pyvista.Plotter()
actor = pl.add_mesh(pyvista.Cone())
pl.set_background('black', top='white')
pl.show()
