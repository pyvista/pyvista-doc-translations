# Create a ParametricFigure8Klein mesh
#
import pyvista
mesh = pyvista.ParametricFigure8Klein()
mesh.plot(color='w', smooth_shading=True)
