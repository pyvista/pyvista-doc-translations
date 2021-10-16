# Compute the point normals of the surface of a sphere.
#
import pyvista as pv
sphere = pv.Sphere()
sphere = sphere.compute_normals(cell_normals=False)
normals = sphere['Normals']
normals.shape
# Expected:
## (842, 3)
#
# Alternatively, create a new mesh when computing the normals
# and compute both cell and point normals.
#
import pyvista as pv
sphere = pv.Sphere()
sphere_with_norm = sphere.compute_normals()
sphere_with_norm.point_data['Normals'].shape
# Expected:
## (842, 3)
sphere_with_norm.cell_data['Normals'].shape
# Expected:
## (1680, 3)
