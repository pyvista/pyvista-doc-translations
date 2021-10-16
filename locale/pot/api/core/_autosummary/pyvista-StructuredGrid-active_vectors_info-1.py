# Create a mesh, compute the normals inplace, set the active
# vectors to the normals, and show that the active vectors are
# the ``'Normals'`` array associated with points.
#
import pyvista
mesh = pyvista.Sphere()
_ = mesh.compute_normals(inplace=True)
mesh.active_vectors_name = 'Normals'
mesh.active_vectors_info
# Expected:
## ActiveArrayInfo(association=<FieldAssociation.POINT: 0>, name='Normals')
