# Create a plotter that we initialize with no lights, and add a
# cube and a single headlight to it.
#
import pyvista as pv
plotter = pv.Plotter(lighting='none')
_ = plotter.add_mesh(pv.Cube())
light = pv.Light(color='cyan', light_type='headlight')
plotter.add_light(light)
plotter.show()
