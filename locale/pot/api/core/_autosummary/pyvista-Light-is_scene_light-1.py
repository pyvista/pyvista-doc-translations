# Verify that none of the lights of the default light kit are
# scene lights.
#
import pyvista as pv
plotter = pv.Plotter()
lights = plotter.renderer.lights
[light.is_scene_light for light in lights]
# Expected:
## [False, False, False, False, False]
