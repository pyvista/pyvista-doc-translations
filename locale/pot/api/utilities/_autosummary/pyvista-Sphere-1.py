# Create a sphere using default parameters.
#
import pyvista
sphere = pyvista.Sphere()
sphere.plot(show_edges=True)
#
# Create a quarter sphere by setting ``end_theta``.
#
sphere = pyvista.Sphere(end_theta=90)
out = sphere.plot(show_edges=True)
