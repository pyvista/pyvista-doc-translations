# Plot three planes lit by three spotlights with varying cone
# angles.  Use a large exponent to cause a visible angular
# variation of the intensity of the beams.
#
import pyvista as pv
plotter = pv.Plotter(lighting='none')
for offset, angle in zip([0, 1.5, 3], [70, 30, 20]):
    _ = plotter.add_mesh(pv.Plane((offset, 0, 0)), color='white')
    light = pv.Light(position=(offset, 0, 1), focal_point=(offset, 0, 0))
    light.exponent = 15
    light.positional = True
    light.cone_angle = angle
    plotter.add_light(light)
plotter.view_xy()
plotter.show()
