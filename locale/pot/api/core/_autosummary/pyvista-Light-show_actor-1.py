# Create a scene containing a cube lit with a cyan spotlight and
# visualize the light using an actor.
#
import pyvista as pv
plotter = pv.Plotter()
_ = plotter.add_mesh(pv.Cube(), color='white')
for light in plotter.renderer.lights:
    light.intensity /= 5
spotlight = pv.Light(position=(-1, 1, 1), color='cyan')
spotlight.positional = True
spotlight.cone_angle = 20
spotlight.intensity = 10
spotlight.exponent = 40
spotlight.show_actor()
plotter.add_light(spotlight)
plotter.show()
