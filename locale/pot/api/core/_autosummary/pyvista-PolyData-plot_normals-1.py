# Plot the point normals of a sphere.
#
import pyvista as pv
sphere = pv.Sphere(phi_resolution=10, theta_resolution=10)
sphere.plot_normals(mag=0.1, show_edges=True)
#
# Plot the face normals of a sphere.
#
import pyvista as pv
sphere = pv.Sphere(phi_resolution=10, theta_resolution=10)
sphere.plot_normals(mag=0.1, faces=True, show_edges=True)
