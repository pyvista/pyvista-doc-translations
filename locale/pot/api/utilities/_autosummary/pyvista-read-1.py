# Load an example mesh.
#
import pyvista
from pyvista import examples
mesh = pyvista.read(examples.antfile)
mesh.plot(cpos='xz')
#
# Load a vtk file.
#
mesh = pyvista.read('my_mesh.vtk')  # doctest:+SKIP
#
# Load a meshio file.
#
mesh = pyvista.read("mesh.obj")  # doctest:+SKIP
