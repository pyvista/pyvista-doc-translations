# Compute the intersection between rays from the origin in
# directions ``[1, 0, 0]``, ``[0, 1, 0]`` and ``[0, 0, 1]``, and
# a sphere with radius 0.5 centered at the origin
#
import pyvista as pv  # doctest:+SKIP
sphere = pv.Sphere()  # doctest:+SKIP
points, rays, cells = sphere.multi_ray_trace([[0, 0, 0]]*3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]], first_point=True)  # doctest:+SKIP
string = ", ".join([f"({point[0]:.3f}, {point[1]:.3f}, {point[2]:.3f})" for point in points]) # doctest:+SKIP
f'Rays intersected at {string}' # doctest:+SKIP
# Expected:
## 'Rays intersected at (0.499, 0.000, 0.000), (0.000, 0.497, 0.000), (0.000, 0.000, 0.500)'
