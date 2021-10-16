# Export and then load back in a theme.
#
import pyvista
theme = pyvista.themes.DefaultTheme()
theme.background = 'white'
theme.save('my_theme.json')  # doctest:+SKIP
loaded_theme = pyvista.load_theme('my_theme.json')  # doctest:+SKIP
