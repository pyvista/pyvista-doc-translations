import pyvista
from pyvista import examples
mesh = examples.load_hexbeam()
another_mesh = examples.load_uniform()
plotter = pyvista.Plotter()
actor = plotter.add_mesh(mesh, color='red')
actor = plotter.add_mesh(another_mesh, color='blue')
plotter.show()
