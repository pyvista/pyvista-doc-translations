# Create a mesh and return the points of the mesh as a numpy
# array.
#
import pyvista
cube = pyvista.Cube()
points = cube.points
points
# Expected:
## pyvista_ndarray([[-0.5, -0.5, -0.5],
##                  [-0.5, -0.5,  0.5],
##                  [-0.5,  0.5,  0.5],
##                  [-0.5,  0.5, -0.5],
##                  [ 0.5, -0.5, -0.5],
##                  [ 0.5,  0.5, -0.5],
##                  [ 0.5,  0.5,  0.5],
##                  [ 0.5, -0.5,  0.5]], dtype=float32)
#
# Shift these points in the z direction and show that their
# position is reflected in the mesh points.
#
points[:, 2] += 1
cube.points
# Expected:
## pyvista_ndarray([[-0.5, -0.5,  0.5],
##                  [-0.5, -0.5,  1.5],
##                  [-0.5,  0.5,  1.5],
##                  [-0.5,  0.5,  0.5],
##                  [ 0.5, -0.5,  0.5],
##                  [ 0.5,  0.5,  0.5],
##                  [ 0.5,  0.5,  1.5],
##                  [ 0.5, -0.5,  1.5]], dtype=float32)
#
# You can also update the points in-place:
#
cube.points[...] = 2*points
cube.points
# Expected:
## pyvista_ndarray([[-1., -1.,  1.],
##                  [-1., -1.,  3.],
##                  [-1.,  1.,  3.],
##                  [-1.,  1.,  1.],
##                  [ 1., -1.,  1.],
##                  [ 1.,  1.,  1.],
##                  [ 1.,  1.,  3.],
##                  [ 1., -1.,  3.]], dtype=float32)
