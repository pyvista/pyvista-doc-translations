import pyvista
from pyvista import examples
filename = examples.download_backward_facing_step(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'foam_case_0_0_0_0.case'
reader = pyvista.get_reader(filename)
reader  # doctest: +ELLIPSIS
# Expected:
## EnSightReader('.../foam_case_0_0_0_0.case')
reader.cell_array_names
# Expected:
## ['v2', 'nut', 'k', 'nuTilda', 'p', 'omega', 'f', 'epsilon', 'U']
reader.point_array_names
# Expected:
## []
reader.all_cell_arrays_status  # doctest: +NORMALIZE_WHITESPACE
# Expected:
## {'v2': True, 'nut': True, 'k': True, 'nuTilda': True, 'p': True, 'omega': True, 'f': True, 'epsilon': True, 'U': True}
reader.disable_all_cell_arrays()
reader.enable_cell_array('U')
mesh = reader.read()  # MultiBlock mesh
mesh[0].array_names
# Expected:
## ['U']
