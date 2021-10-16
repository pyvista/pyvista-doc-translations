# Clip a sphere in the X direction centered at the origin.  This
# will leave behind half a sphere in the positive X direction.
#
import pyvista as pv
sphere = pv.Sphere()
clipped_mesh = sphere.clip_closed_surface('-z')
clipped_mesh.plot(show_edges=True, line_width=3)
#
# Clip the sphere at the XY plane and leave behind half the
# sphere in the positive Z direction.  Shift the clip upwards to
# leave a smaller mesh behind.
#
clipped_mesh = sphere.clip_closed_surface('z', origin=[0, 0, 0.3])
clipped_mesh.plot(show_edges=True, line_width=3)
