# Create a mesh, add scalars to the mesh, and return the name of
# the active scalars.
#
import pyvista
mesh = pyvista.Sphere()
mesh['Z Height'] = mesh.points[:, 2]
mesh.active_scalars_name
# Expected:
## 'Z Height'
