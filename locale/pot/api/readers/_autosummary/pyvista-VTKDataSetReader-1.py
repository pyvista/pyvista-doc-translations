import pyvista
from pyvista import examples
filename = examples.download_brain(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'brain.vtk'
reader = pyvista.get_reader(filename)
mesh = reader.read()
sliced_mesh = mesh.slice('x')
sliced_mesh.plot(cpos='yz', show_scalar_bar=False)
