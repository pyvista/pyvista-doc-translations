import pyvista
from pyvista import examples
filename = examples.download_cad_model(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## '42400-IDGH.stl'
reader = pyvista.get_reader(filename)
mesh = reader.read()
mesh.plot()
