# Create a light at (10, 10, 10) and set its diffuse color to red.
#
import pyvista as pv
light = pv.Light(position=(10, 10, 10))
light.diffuse_color = 1, 0, 0
#
# Create a positional light at (0, 0, 3) with a cone angle of
# 30, exponent of 20, and a visible actor.
#
light = pv.Light(position=(0, 0, 3), show_actor=True,
                 positional=True, cone_angle=30, exponent=20)
