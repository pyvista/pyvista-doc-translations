# Create a 2 wide plot and set the background of right-hand plot
# to orange.  Add a cube to the left plot and a sphere to the
# right.
#
import pyvista
pl = pyvista.Plotter(shape=(1, 2))
actor = pl.add_mesh(pyvista.Cube())
pl.subplot(0, 1)
actor = pl.add_mesh(pyvista.Sphere())
pl.set_background('orange', all_renderers=False)
pl.show()
