# Clip a cube along the +X direction.  ``triangulate`` is used as
# the cube is initially composed of quadrilateral faces and
# subdivide only works on triangles.
#
import pyvista as pv
cube = pv.Cube().triangulate().subdivide(3)
clipped_cube = cube.clip()
clipped_cube.plot()
#
# Clip a cube in the +Z direction.  This leaves half a cube
# below the XY plane.
#
import pyvista as pv
cube = pv.Cube().triangulate().subdivide(3)
clipped_cube = cube.clip('z')
clipped_cube.plot()
