# Isometric view.
#
from pyvista import demos
pl = demos.orientation_plotter()
pl.view_isometric()
pl.show()
#
# Negative isometric view.
#
from pyvista import demos
pl = demos.orientation_plotter()
pl.view_isometric(negative=True)
pl.show()
