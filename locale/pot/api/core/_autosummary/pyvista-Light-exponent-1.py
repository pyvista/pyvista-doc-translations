# Plot three planes lit by three spotlights with exponents of 1,
# 2 and 5.  The one with the lowest exponent has the broadest
# beam.
#
import pyvista as pv
plotter = pv.Plotter(lighting='none')
for offset, exponent in zip([0, 1.5, 3], [1, 2, 5]):
    _ = plotter.add_mesh(pv.Plane((offset, 0, 0)), color='white')
    light = pv.Light(position=(offset, 0, 0.1), focal_point=(offset, 0, 0))
    light.exponent = exponent
    light.positional = True
    light.cone_angle = 80
    plotter.add_light(light)
plotter.view_xy()
plotter.show()
