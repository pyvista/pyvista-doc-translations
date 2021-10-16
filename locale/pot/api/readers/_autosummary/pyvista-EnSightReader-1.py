import pyvista
from pyvista import examples
filename = examples.download_cylinder_crossflow(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'cylinder_Re35.case'
reader = pyvista.get_reader(filename)
mesh = reader.read()
mesh.plot(scalars="velocity", component=1, clim=[-20, 20], 
          cpos='xy', cmap='RdBu', show_scalar_bar=False)
