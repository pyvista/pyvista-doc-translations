# Extract the edges from an unstructured grid.
#
import pyvista
from pyvista import examples
hex_beam = pyvista.read(examples.hexbeamfile)
feat_edges = hex_beam.extract_feature_edges()
feat_edges.clear_data()  # clear array data for plotting
feat_edges.plot(line_width=10)
