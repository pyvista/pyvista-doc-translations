# Compute the intersection between a ray from the origin to
# ``[1, 0, 0]`` and a sphere with radius 0.5 centered at the
# origin.
#
import pyvista as pv
sphere = pv.Sphere()
point, cell = sphere.ray_trace([0, 0, 0], [1, 0, 0], first_point=True)
f'Intersected at {point[0]:.3f} {point[1]:.3f} {point[2]:.3f}'
# Expected:
## 'Intersected at 0.499 0.000 0.000'
#
# Show a plot of the ray trace.
#
point, cell = sphere.ray_trace([0, 0, 0], [1, 0, 0], plot=True)
