# Add field data to a PolyData dataset and then remove it.
#
import pyvista
mesh = pyvista.Sphere()
mesh.field_data['my-field-data'] = range(10)
len(mesh.field_data)
# Expected:
## 1
mesh.clear_field_data()
len(mesh.field_data)
# Expected:
## 0
