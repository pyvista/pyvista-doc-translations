# Clear the texture from the globe example.
#
from pyvista import examples
globe = examples.load_globe()
globe.textures
# Expected:
## {'2k_earth_daymap': ...}
globe.clear_textures()
globe.textures
# Expected:
## {}
