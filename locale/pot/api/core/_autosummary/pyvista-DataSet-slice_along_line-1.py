# Slice the random hills dataset along a circular arc.
#
import numpy as np
import pyvista
from pyvista import examples
hills = examples.load_random_hills()
center = np.array(hills.center)
point_a = center + np.array([5, 0, 0])
point_b = center + np.array([-5, 0, 0])
arc = pyvista.CircularArc(point_a, point_b, center, resolution=100)
line_slice = hills.slice_along_line(arc)
#
# Plot the circular arc and the hills mesh.
#
pl = pyvista.Plotter()
_ = pl.add_mesh(hills, smooth_shading=True, style='wireframe')
_ = pl.add_mesh(line_slice, line_width=10, render_lines_as_tubes=True,
                color='k')
_ = pl.add_mesh(arc, line_width=10, color='grey')
pl.show()
