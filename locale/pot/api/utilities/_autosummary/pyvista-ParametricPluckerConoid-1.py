# Create a ParametricPluckerConoid mesh.
#
import pyvista
mesh = pyvista.ParametricPluckerConoid()
mesh.plot(color='w', smooth_shading=True)
