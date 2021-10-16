# Create a ParametricSuperToroid mesh.
#
import pyvista
mesh = pyvista.ParametricSuperToroid(n1=2, n2=0.3)
mesh.plot(color='w', smooth_shading=True)
