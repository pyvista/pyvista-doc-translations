# Decimate a sphere.  First plot the sphere.
#
import pyvista
sphere = pyvista.Sphere(phi_resolution=60, theta_resolution=60)
sphere.plot(show_edges=True, line_width=2)
#
# Now decimate it by 75% and plot it.
#
decimated = sphere.decimate(0.75)
decimated.plot(show_edges=True, line_width=2)
