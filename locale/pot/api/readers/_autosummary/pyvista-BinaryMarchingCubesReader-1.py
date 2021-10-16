import pyvista
from pyvista import examples
filename = examples.download_pine_roots(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'pine_root.tri'
reader = pyvista.get_reader(filename)
mesh = reader.read()
mesh.plot(color="brown")
