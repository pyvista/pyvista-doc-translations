# Create a light and set its ambient color to red.
#
import pyvista
light = pyvista.Light()
light.ambient_color = 'red'
light.ambient_color
# Expected:
## (1.0, 0.0, 0.0)
