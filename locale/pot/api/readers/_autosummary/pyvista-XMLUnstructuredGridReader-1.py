import pyvista
from pyvista import examples
filename = examples.download_notch_displacement(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'notch_disp.vtu'
reader = pyvista.get_reader(filename)
mesh = reader.read()
mesh.plot(scalars="Nodal Displacement", component=0,
          cpos='xy', show_scalar_bar=False)
