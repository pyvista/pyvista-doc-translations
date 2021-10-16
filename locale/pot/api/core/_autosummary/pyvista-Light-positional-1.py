# Create a spotlight shining on the origin.
#
import pyvista as pv
light = pv.Light(position=(1, 1, 1))
light.positional = True
light.cone_angle = 30
