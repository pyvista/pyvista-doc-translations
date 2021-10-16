# Return the cell connectivity for the first two cells.
import pyvista
from pyvista import examples
hex_beam = pyvista.read(examples.hexbeamfile)
hex_beam.cell_connectivity[:16]
# Expected:
## array([ 0,  2,  8,  7, 27, 36, 90, 81,  2,  1,  4,  8, 36, 18, 54, 90])
