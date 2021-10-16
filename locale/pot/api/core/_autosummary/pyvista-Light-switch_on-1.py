# Create a light, switch it off and switch it back on again.
#
import pyvista as pv
light = pv.Light()
light.on = False
light.switch_on()
