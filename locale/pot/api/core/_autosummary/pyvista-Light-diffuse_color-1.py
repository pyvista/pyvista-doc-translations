# Create a light and set its diffuse color to blue.
#
import pyvista as pv
light = pv.Light()
light.diffuse_color = (0, 0, 1)
light.diffuse_color
# Expected:
## (0.0, 0.0, 1.0)
