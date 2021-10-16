# Create a light and set its specular color to bright green.
#
import pyvista as pv
light = pv.Light()
light.specular_color = '#00FF00'
light.specular_color
# Expected:
## (0.0, 1.0, 0.0)
