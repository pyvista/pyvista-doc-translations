# Flatten a sphere to the XY plane.
#
import pyvista as pv
sphere = pv.Sphere()
projected = sphere.project_points_to_plane()
projected.plot(show_edges=True, line_width=3)
