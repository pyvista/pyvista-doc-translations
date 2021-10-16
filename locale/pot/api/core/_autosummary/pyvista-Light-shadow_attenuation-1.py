# Set the shadow attenuation to 0.5
#
import pyvista as pv
light = pv.Light()
light.shadow_attenuation = 0.5
light.shadow_attenuation
# Expected:
## 0.5
