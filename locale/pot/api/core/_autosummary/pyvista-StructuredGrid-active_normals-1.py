# Compute normals on an example sphere mesh and return the
# active normals for the dataset.  Show that this is the same size
# as the number of points.
#
import pyvista
mesh = pyvista.Sphere()
mesh = mesh.compute_normals()
normals = mesh.active_normals
normals.shape
# Expected:
## (842, 3)
mesh.n_points
# Expected:
## 842
