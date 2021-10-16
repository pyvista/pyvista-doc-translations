# Plot three cubes lit by two lights with different attenuation
# profiles.  The blue light has slower linear attenuation, the
# green one has quadratic attenuation that makes it decay
# faster. Note that there are no shadow effects included so each
# box gets lit by both lights.
#
import pyvista as pv
plotter = pv.Plotter(lighting='none')
for offset in 1, 2.5, 4:
    _ = plotter.add_mesh(pv.Cube(center=(offset, offset, 0)), color='white')
colors = ['b', 'g']
all_attenuations = [(0, 0.1, 0), (0, 0, 0.1)]
centers = [(0, 1, 0), (1, 0, 0)]
for color, attenuation_constants, center in zip(colors, all_attenuations, centers):
    light = pv.Light(position=center, color=color)
    light.focal_point = (1 + center[0], 1 + center[1], 0)
    light.cone_angle = 90
    light.positional = True
    light.attenuation_values = attenuation_constants
    plotter.add_light(light)
plotter.view_vector((-1, -1, 1))
plotter.show()
