import pyvista
from pyvista import examples
filename = examples.download_human(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'Human.vtp'
reader = pyvista.get_reader(filename)
reader  # doctest: +ELLIPSIS
# Expected:
## XMLPolyDataReader('.../Human.vtp')
mesh = reader.read()
mesh # doctest: +ELLIPSIS
# Expected:
## PolyData ...
mesh.plot(color='tan')
