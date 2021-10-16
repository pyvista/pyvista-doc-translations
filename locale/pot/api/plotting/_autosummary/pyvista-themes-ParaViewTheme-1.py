# Make the paraview-like theme the global default.
#
import pyvista
from pyvista import themes
pyvista.set_plot_theme(themes.ParaViewTheme())
#
# Alternatively, set via a string.
#
pyvista.set_plot_theme('paraview')
