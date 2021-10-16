import pyvista as pv
plane = pv.Plane(i_resolution=2, j_resolution=2)
plane.faces
# Expected:
## array([4, 0, 1, 4, 3, 4, 1, 2, 5, 4, 4, 3, 4, 7, 6, 4, 4, 5, 8, 7])
#
# Note how the faces contain a "padding" indicating the number
# of points per face:
#
plane.faces.reshape(-1, 5)
# Expected:
## array([[4, 0, 1, 4, 3],
##        [4, 1, 2, 5, 4],
##        [4, 3, 4, 7, 6],
##        [4, 4, 5, 8, 7]])
