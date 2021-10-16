# Check the type of lights for the first two lights of the default
# light kit of plotters.
#
import pyvista as pv
plotter = pv.Plotter()
lights = plotter.renderer.lights[:2]
[light.light_type for light in lights]
# Expected:
## [<LightType.HEADLIGHT: 1>, <LightType.CAMERA_LIGHT: 2>]
#
# Change the light type of the default light kit's headlight to a scene light.
#
import pyvista as pv
plotter = pv.Plotter()
lights = plotter.renderer.lights[:2]
lights[0].light_type = pv.Light.SCENE_LIGHT
[light.light_type for light in lights]
# Expected:
## [<LightType.SCENE_LIGHT: 3>, <LightType.CAMERA_LIGHT: 2>]
