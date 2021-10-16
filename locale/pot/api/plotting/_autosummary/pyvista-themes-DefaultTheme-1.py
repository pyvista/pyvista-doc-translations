# Change the global default background color to white.
#
import pyvista
pyvista.global_theme.color = 'white'
#
# Show edges by default.
#
pyvista.global_theme.show_edges = True
#
# Create a new theme from the default theme and apply it globally.
#
my_theme = pyvista.themes.DefaultTheme()
my_theme.color = 'red'
my_theme.background = 'white'
pyvista.global_theme.load_theme(my_theme)
