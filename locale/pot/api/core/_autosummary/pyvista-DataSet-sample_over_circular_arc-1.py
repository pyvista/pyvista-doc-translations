# Sample a dataset over a circular arc and plot it.
#
import pyvista
from pyvista import examples
uniform = examples.load_uniform()
uniform["height"] = uniform.points[:, 2]
pointa = [uniform.bounds[1], uniform.bounds[2], uniform.bounds[5]]
pointb = [uniform.bounds[1], uniform.bounds[3], uniform.bounds[4]]
center = [uniform.bounds[1], uniform.bounds[2], uniform.bounds[4]]
sampled_arc = uniform.sample_over_circular_arc(pointa, pointb, center)
pl = pyvista.Plotter()
_ = pl.add_mesh(uniform, style='wireframe')
_ = pl.add_mesh(sampled_arc, line_width=10)
pl.show_axes()
pl.show()
