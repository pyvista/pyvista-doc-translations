# Clip a cube with a sphere.
#
import pyvista
sphere = pyvista.Sphere(center=(-0.4, -0.4, -0.4))
cube = pyvista.Cube().triangulate().subdivide(3)
clipped = cube.clip_surface(sphere)
clipped.plot(show_edges=True, cpos='xy', line_width=3)
#
# See :ref:`clip_with_surface_example` for more examples using
