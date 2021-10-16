# Look from the top down by setting view up to ``[0, 1, 0]``.
# Notice how the Y axis appears vertical.
#
from pyvista import demos
pl = demos.orientation_plotter()
pl.set_viewup([0, 1, 0])
pl.show()
