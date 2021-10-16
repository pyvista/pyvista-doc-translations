# Create a custom theme from the default theme and load it into
# the global theme of pyvista.
#
import pyvista
from pyvista.themes import DefaultTheme
my_theme = DefaultTheme()
my_theme.font.size = 20
my_theme.font.title_size = 40
my_theme.cmap = 'jet'
pyvista.global_theme.load_theme(my_theme)
pyvista.global_theme.font.size
# Expected:
## 20
#
# Create a custom theme from the dark theme and load it into
# pyvista.
#
from pyvista.themes import DarkTheme
my_theme = DarkTheme()
my_theme.show_edges = True
pyvista.global_theme.load_theme(my_theme)
pyvista.global_theme.show_edges
# Expected:
## True
