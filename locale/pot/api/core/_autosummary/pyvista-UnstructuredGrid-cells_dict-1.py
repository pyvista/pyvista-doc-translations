# Return the cells dictionary of the sample hex beam.  Note how
# there is only one key/value pair as the hex beam example is
# composed of only all hexahedral cells, which is
# ``vtk.VTK_HEXAHEDRON``, which evaluates to 12.
#
# Also note how there is no padding for the cell array.  This
# approach may be more helpful than the ``cells`` property when
# extracting cells.
#
import pyvista
from pyvista import examples
hex_beam = pyvista.read(examples.hexbeamfile)
hex_beam.cells_dict  # doctest:+SKIP
# Expected:
## {12: array([[ 0,  2,  8,  7, 27, 36, 90, 81],
##         [ 2,  1,  4,  8, 36, 18, 54, 90],
##         [ 7,  8,  6,  5, 81, 90, 72, 63],
##         ...
##         [44, 26, 62, 98, 11, 10, 13, 17],
##         [89, 98, 80, 71, 16, 17, 15, 14],
##         [98, 62, 53, 80, 17, 13, 12, 15]])}
