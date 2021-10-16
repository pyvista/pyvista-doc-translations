# Show a mesh from :func:`pyvista.Plane` is not composed of all
# triangles.
#
import pyvista
plane = pyvista.Plane()
plane.is_all_triangles
# Expected:
## False <CallableBool>
#
# Show that the mesh from :func:`pyvista.Sphere` contains only
# triangles.
#
sphere = pyvista.Sphere()
sphere.is_all_triangles
# Expected:
## True <CallableBool>
