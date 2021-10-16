# Create a ParametricBohemianDome mesh.
#
import pyvista
mesh = pyvista.ParametricBohemianDome()
mesh.plot(color='w', smooth_shading=True)
