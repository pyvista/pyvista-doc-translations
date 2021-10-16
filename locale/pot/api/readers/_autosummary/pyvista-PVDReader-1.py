import pyvista
from pyvista import examples
filename = examples.download_wavy(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'wavy.pvd'
reader = pyvista.get_reader(filename)
reader.time_values  # doctest: +ELLIPSIS
# Expected:
## [0.0, 1.0, 2.0, 3.0, ... 12.0, 13.0, 14.0]
reader.set_active_time_point(5)
reader.active_time_value
# Expected:
## 5.0
mesh = reader.read()[0]  # MultiBlock mesh with only 1 block
mesh.plot(scalars='z')
