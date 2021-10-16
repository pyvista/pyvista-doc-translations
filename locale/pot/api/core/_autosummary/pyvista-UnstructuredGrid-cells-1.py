# Return the indices of the first two cells from the example hex
# beam.  Note how the cells have "padding" indicating the number
# of points per cell.
#
import pyvista
from pyvista import examples
hex_beam = pyvista.read(examples.hexbeamfile)
hex_beam.cells[:18]  # doctest:+SKIP
# Expected:
## array([ 8,  0,  2,  8,  7, 27, 36, 90, 81,  8,  2,  1,  4,  
##         8, 36, 18, 54, 90])
