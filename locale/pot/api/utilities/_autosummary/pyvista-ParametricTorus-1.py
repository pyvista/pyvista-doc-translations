# Create a ParametricTorus mesh.
#
import pyvista
mesh = pyvista.ParametricTorus()
mesh.plot(color='w', smooth_shading=True)
