# Create a ParametricEllipsoid mesh
#
import pyvista
mesh = pyvista.ParametricEllipsoid()
mesh.plot(color='w', smooth_shading=True)
