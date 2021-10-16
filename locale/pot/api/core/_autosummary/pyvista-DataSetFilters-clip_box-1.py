# Clip a corner of a cube.  The bounds of a cube are normally
# ``[-0.5, 0.5, -0.5, 0.5, -0.5, 0.5]``, and this removes 1/8 of
# the cube's surface.
#
import pyvista as pv
cube = pv.Cube().triangulate().subdivide(3)
clipped_cube = cube.clip_box([0, 1, 0, 1, 0, 1])
clipped_cube.plot()
