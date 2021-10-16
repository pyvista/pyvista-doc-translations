# Create a light that shines on the origin from a 30-degree
# elevation in the xz plane.
#
import pyvista as pv
light = pv.Light()
light.set_direction_angle(30, 0)
