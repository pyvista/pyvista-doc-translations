# Plot the path between two points on the random hills mesh.
#
import pyvista as pv
from pyvista import examples
hills = examples.load_random_hills()
path = hills.geodesic(560, 5820)
pl = pv.Plotter()
_ = pl.add_mesh(hills)
_ = pl.add_mesh(path, line_width=5, color='k')
pl.show()
