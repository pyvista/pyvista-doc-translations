# Return the cell offset array within ``vtk==9``.  Since this
# mesh is composed of all hexahedral cells, note how each cell
# starts at 8 greater than the prior cell.
#
import pyvista
from pyvista import examples
hex_beam = pyvista.read(examples.hexbeamfile)
hex_beam.offset
# Expected:
## array([  0,   8,  16,  24,  32,  40,  48,  56,  64,  72,  80,  88,  96,
##        104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200,
##        208, 216, 224, 232, 240, 248, 256, 264, 272, 280, 288, 296, 304,
##        312, 320])
