# Set the scale in the z direction to be 5 times that of
# nominal.  Leave the other axes unscaled.
#
import pyvista
pl = pyvista.Plotter()
pl.set_scale(zscale=5)
_ = pl.add_mesh(pyvista.Sphere())  # perfect sphere
pl.show()
