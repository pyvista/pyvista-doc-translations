# Generate and plot the outline of a sphere.  This is
# effectively the ``(x, y, z)`` bounds of the mesh.
#
import pyvista
sphere = pyvista.Sphere()
outline = sphere.outline()
pyvista.plot([sphere, outline], line_width=5)
