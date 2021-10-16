import pyvista as pv
data = [pv.Sphere(center=(2, 0, 0)), pv.Cube(center=(0, 2, 0)), pv.Cone()]
blocks = pv.MultiBlock(data)
blocks.center  # doctest:+SKIP
# Expected:
## array([1., 1., 0.])
