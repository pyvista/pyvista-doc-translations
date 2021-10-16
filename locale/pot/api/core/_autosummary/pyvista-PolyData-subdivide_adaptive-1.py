# First, load the example airplane mesh and plot it.
#
import pyvista
from pyvista import examples
mesh = pyvista.PolyData(examples.planefile)
mesh.plot(show_edges=True, line_width=3)
#
# Subdivide the mesh
#
submesh = mesh.subdivide_adaptive(max_n_passes=2)
submesh.plot(show_edges=True)
