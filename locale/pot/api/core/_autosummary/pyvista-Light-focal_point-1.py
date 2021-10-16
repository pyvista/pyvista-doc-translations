# Create a light at (10, 10, 10) shining at (0, 0, 1).
#
import pyvista as pv
light = pv.Light(position=(10, 10, 10))
light.focal_point = (0, 0, 1)
