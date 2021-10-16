# Generate and plot the corners of a sphere.  This is
# effectively the ``(x, y, z)`` bounds of the mesh.
#
import pyvista
sphere = pyvista.Sphere()
corners = sphere.outline_corners(factor=0.1)
pyvista.plot([sphere, corners], line_width=5)
