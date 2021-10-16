import pyvista as pv

plotter = pv.Plotter(lighting=None, window_size=(800, 800))

# create a top down light
light = pv.Light(position=(0, 0, 3), show_actor=True, positional=True,
                 cone_angle=30, exponent=20, intensity=1.5)
plotter.add_light(light)

# add a sphere to the plotter
sphere = pv.Sphere(radius=0.3, center=(0, 0, 1))
plotter.add_mesh(sphere, ambient=0.2, diffuse=0.5, specular=0.8,
                 specular_power=30, smooth_shading=True,
                 color='dodgerblue')

# add the grid
grid = pv.Plane(i_size=4, j_size=4)
plotter.add_mesh(grid, ambient=0, diffuse=0.5, specular=0.8, color='white')

# setup and show the plotter
plotter.enable_shadows()
plotter.set_background('darkgrey')
plotter.show()