# Return the active texture datasets from the globe example.
#
from pyvista import examples
globe = examples.load_globe()
globe.textures
# Expected:
## {'2k_earth_daymap': (Texture)...}
