import pyvista
from pyvista import examples
mesh = examples.load_hexbeam()
othermesh = examples.load_uniform()
plotter = pyvista.Plotter()
_ = plotter.add_mesh(mesh, label='My Mesh')
_ = plotter.add_mesh(othermesh, 'k', label='My Other Mesh')
_ = plotter.add_legend()
plotter.show()
#
# Alternative manual example
#
import pyvista
from pyvista import examples
mesh = examples.load_hexbeam()
othermesh = examples.load_uniform()
legend_entries = []
legend_entries.append(['My Mesh', 'w'])
legend_entries.append(['My Other Mesh', 'k'])
plotter = pyvista.Plotter()
_ = plotter.add_mesh(mesh)
_ = plotter.add_mesh(othermesh, 'k')
_ = plotter.add_legend(legend_entries)
plotter.show()
