# Sample a dataset over a circular arc.
#
import pyvista
from pyvista import examples
uniform = examples.load_uniform()
uniform["height"] = uniform.points[:, 2]
normal = [0, 0, 1]
polar = [0, 9, 0]
center = [uniform.bounds[1], uniform.bounds[2], uniform.bounds[5]]
arc = uniform.sample_over_circular_arc_normal(center, normal=normal,
                                              polar=polar)
pl = pyvista.Plotter()
_ = pl.add_mesh(uniform, style='wireframe')
_ = pl.add_mesh(arc, line_width=10)
pl.show_axes()
pl.show()
