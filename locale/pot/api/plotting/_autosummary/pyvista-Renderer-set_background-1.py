# Set the background color to black with a gradient to white at
# the top of the plot.
#
import pyvista
pl = pyvista.Plotter()
actor = pl.add_mesh(pyvista.Cone())
pl.set_background('black', top='white')
pl.show()
