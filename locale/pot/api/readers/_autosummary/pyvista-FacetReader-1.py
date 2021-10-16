import pyvista
from pyvista import examples
filename = examples.download_clown(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'clown.facet'
reader = pyvista.get_reader(filename)
mesh = reader.read()
mesh.plot(color="red")
