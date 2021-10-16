# Create a DataSet with a variety of arrays.
#
import pyvista
mesh = pyvista.Cube()
mesh.clear_data()
mesh.point_data['point-data'] = range(mesh.n_points)
mesh.cell_data['cell-data'] = range(mesh.n_cells)
mesh.field_data['field-data'] = ['a', 'b', 'c']
mesh.array_names
# Expected:
## ['point-data', 'field-data', 'cell-data']
#
# Get the point data array association.
#
mesh.get_array_association('point-data')
# Expected:
## <FieldAssociation.POINT: 0>
#
# Get the cell data array association.
#
mesh.get_array_association('cell-data')
# Expected:
## <FieldAssociation.CELL: 1>
#
# Get the field data array association.
#
mesh.get_array_association('field-data')
# Expected:
## <FieldAssociation.NONE: 2>
