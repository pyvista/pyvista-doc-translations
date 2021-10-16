# Create a ParametricSuperEllipsoid surface that looks like a box
# with smooth edges.
#
import pyvista
mesh = pyvista.ParametricSuperEllipsoid(n1=0.02, n2=0.02)
mesh.plot(color='w', smooth_shading=True)
#
# Create one that looks like a spinning top.
#
mesh = pyvista.ParametricSuperEllipsoid(n1=4, n2=0.5)
mesh.plot(color='w', smooth_shading=True, cpos='xz')
