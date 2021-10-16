# Remove the first 100 points from a sphere.
#
import pyvista as pv
sphere = pv.Sphere()
reduced_sphere, ridx = sphere.remove_points(range(100, 250))
reduced_sphere.plot(show_edges=True, line_width=3)
