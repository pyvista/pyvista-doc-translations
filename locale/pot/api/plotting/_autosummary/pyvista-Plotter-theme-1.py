# Use the dark theme for a plotter.
#
import pyvista
from pyvista import themes
pl = pyvista.Plotter()
pl.theme = themes.DarkTheme()
actor = pl.add_mesh(pyvista.Sphere())
pl.show()
