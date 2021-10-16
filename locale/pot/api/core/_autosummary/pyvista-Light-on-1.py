# Create a light, check if it's on by default, and turn it off.
#
import pyvista as pv
light = pv.Light()
light.on
# Expected:
## True
light.on = False
