# Cast a :class:`pyvista.PolyData` to a
# :class:`pyvista.UnstructuredGrid`.
#
import pyvista
mesh = pyvista.Sphere()
type(mesh)
# Expected:
## <class 'pyvista.core.pointset.PolyData'>
grid = mesh.cast_to_unstructured_grid()
type(grid)
# Expected:
## <class 'pyvista.core.pointset.UnstructuredGrid'>
