# Verify that four out of five lights of the default light kit
# are camera lights.
#
import pyvista as pv
plotter = pv.Plotter()
lights = plotter.renderer.lights
[light.is_camera_light for light in lights]
# Expected:
## [False, True, True, True, True]
