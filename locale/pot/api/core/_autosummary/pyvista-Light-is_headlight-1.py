# Verify that the first light of the default light kit is a headlight.
#
import pyvista as pv
plotter = pv.Plotter()
lights = plotter.renderer.lights
[light.is_headlight for light in lights]
# Expected:
## [True, False, False, False, False]
