# Create a mesh, compute the normals inplace, and return the
# normals vector array.
#
import pyvista
mesh = pyvista.Sphere()
_ = mesh.compute_normals(inplace=True)
mesh.active_vectors  # doctest:+SKIP
# Expected:
## pyvista_ndarray([[-2.48721432e-10, -1.08815623e-09, -1.00000000e+00],
##                  [-2.48721432e-10, -1.08815623e-09,  1.00000000e+00],
##                  [-1.18888125e-01,  3.40539310e-03, -9.92901802e-01],
##                  ...,
##                  [-3.11940581e-01, -6.81432486e-02,  9.47654784e-01],
##                  [-2.09880397e-01, -4.65070531e-02,  9.76620376e-01],
##                  [-1.15582108e-01, -2.80492082e-02,  9.92901802e-01]],
##                 dtype=float32)
