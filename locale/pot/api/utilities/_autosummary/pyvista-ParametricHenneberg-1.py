# Create a ParametricHenneberg mesh
#
import pyvista
mesh = pyvista.ParametricHenneberg()
mesh.plot(color='w', smooth_shading=True)
