# Show the viewport of a renderer taking up half the render
# window.
#
import pyvista
pl = pyvista.Plotter(shape=(1, 2))
pl.renderers[0].viewport
# Expected:
## (0.0, 0.0, 0.5, 1.0)
