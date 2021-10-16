# First, create an example coarse sphere mesh and plot it.
#
from pyvista import examples
import pyvista
mesh = pyvista.Sphere(phi_resolution=10, theta_resolution=10)
mesh.plot(show_edges=True, line_width=3)
#
# Subdivide the sphere mesh using linear subdivision.
#
submesh = mesh.subdivide(1, 'linear')
submesh.plot(show_edges=True, line_width=3)
#
# Subdivide the sphere mesh using loop subdivision.
#
submesh = mesh.subdivide(1, 'loop')
submesh.plot(show_edges=True, line_width=3)
#
# Subdivide the sphere mesh using butterfly subdivision.
#
submesh = mesh.subdivide(1, 'butterfly')
submesh.plot(show_edges=True, line_width=3)
