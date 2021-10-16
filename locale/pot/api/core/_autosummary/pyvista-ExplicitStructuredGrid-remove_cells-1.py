# Remove 20 cells from an unstructured grid.
#
from pyvista import examples
import pyvista
hex_mesh = pyvista.read(examples.hexbeamfile)
removed = hex_mesh.remove_cells(range(10, 20))
removed.plot(color='tan', show_edges=True, line_width=3)
