import pyvista
from pyvista import examples
filename = examples.download_lobster(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'lobster.ply'
reader = pyvista.get_reader(filename)
mesh = reader.read()
mesh.plot()
