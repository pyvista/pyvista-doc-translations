# Make the document theme the global default.
#
import pyvista
from pyvista import themes
pyvista.set_plot_theme(themes.DocumentTheme())
#
# Alternatively, set via a string.
#
pyvista.set_plot_theme('document')
