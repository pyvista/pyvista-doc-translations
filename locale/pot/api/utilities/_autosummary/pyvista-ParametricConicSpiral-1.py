# Create a ParametricConicSpiral mesh.
#
import pyvista
mesh = pyvista.ParametricConicSpiral()
mesh.plot(color='w', smooth_shading=True)
