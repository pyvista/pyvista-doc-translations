# Compute the face area of the example airplane mesh.
#
from pyvista import examples
surf = examples.load_airplane()
surf = surf.compute_cell_sizes(length=False, volume=False)
surf.plot(show_edges=True)
