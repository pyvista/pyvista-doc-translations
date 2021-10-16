# Create a ParametricPseudosphere mesh.
#
import pyvista
mesh = pyvista.ParametricPseudosphere()
mesh.plot(color='w', smooth_shading=True)
