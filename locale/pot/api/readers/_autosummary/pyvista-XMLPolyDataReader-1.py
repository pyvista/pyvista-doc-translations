import pyvista
from pyvista import examples
filename = examples.download_cow_head(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'cowHead.vtp'
reader = pyvista.get_reader(filename)
mesh = reader.read()
mesh.plot(
   cpos=((12, 3.5, -4.5), (4.5, 1.6, 0), (0, 1, 0.3)),
   clim=[0, 100], show_scalar_bar=False
)
