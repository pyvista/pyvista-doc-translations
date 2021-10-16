# Slice the surface of a sphere.
#
import pyvista
sphere = pyvista.Sphere()
slice_x = sphere.slice(normal='x')
slice_y = sphere.slice(normal='y')
slice_z = sphere.slice(normal='z')
slices = slice_x + slice_y + slice_z
slices.plot(line_width=5)
