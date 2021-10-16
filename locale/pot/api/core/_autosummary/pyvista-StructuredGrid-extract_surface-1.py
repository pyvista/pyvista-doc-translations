# Extract the surface of an UnstructuredGrid.
#
import pyvista
from pyvista import examples
grid = examples.load_hexbeam()
surf = grid.extract_surface()
type(surf)
# Expected:
## <class 'pyvista.core.pointset.PolyData'>
