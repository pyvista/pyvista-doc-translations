# Generate a 3D Delaunay triangulation of a surface mesh of a
# sphere and plot the interior edges generated.
#
import pyvista
sphere = pyvista.Sphere(theta_resolution=5, phi_resolution=5)
grid = sphere.delaunay_3d()
edges = grid.extract_all_edges()
edges.plot(line_width=5, color='k')
