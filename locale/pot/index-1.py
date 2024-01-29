import pyvista
pyvista.set_jupyter_backend('static')
pyvista.global_theme.background = 'white'
pyvista.global_theme.window_size = [600, 400]
pyvista.global_theme.axes.show = False
pyvista.global_theme.smooth_shading = True
pyvista.global_theme.anti_aliasing = 'fxaa'