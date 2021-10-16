# Extract the edges of a sample unstructured grid and plot the edges.
# Note how it plots interior edges.
#
import pyvista
from pyvista import examples
hex_beam = pyvista.read(examples.hexbeamfile)
edges = hex_beam.extract_all_edges()
edges.plot(line_width=5, color='k')
