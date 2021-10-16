import pyvista
from pyvista import examples
filename = examples.download_structured_grid(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'StructuredGrid.vts'
reader = pyvista.get_reader(filename)
mesh = reader.read()
mesh.plot(style='wireframe', line_width=4, show_scalar_bar=False)
