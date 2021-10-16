# This mesh contains only linear hexahedral cells, type
# ``vtk.VTK_HEXAHEDRON``, which evaluates to 12.
#
import pyvista
from pyvista import examples
hex_beam = pyvista.read(examples.hexbeamfile)
hex_beam.celltypes  # doctest:+SKIP
# Expected:
## array([12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
##        12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
##        12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
##        dtype=uint8)
