# Load an example mesh using the legacy reader.
#
import pyvista
from pyvista import examples
mesh = pyvista.read_legacy(examples.uniformfile)
