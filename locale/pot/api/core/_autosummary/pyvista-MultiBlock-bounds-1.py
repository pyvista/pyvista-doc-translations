# Return the bounds across blocks.
#
import pyvista as pv
data = [pv.Sphere(center=(2, 0, 0)), pv.Cube(center=(0, 2, 0)), pv.Cone()]
blocks = pv.MultiBlock(data)
blocks.bounds
# Expected:
## [-0.5, 2.5, -0.5, 2.5, -0.5, 0.5]
