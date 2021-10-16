# Compute and plot the minimum angle of a sample sphere mesh.
#
import pyvista
sphere = pyvista.Sphere(theta_resolution=20, phi_resolution=20)
cqual = sphere.compute_cell_quality('min_angle')
cqual.plot(show_edges=True)
