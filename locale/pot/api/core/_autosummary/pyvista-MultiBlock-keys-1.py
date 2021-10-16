import pyvista as pv
data = {"cube": pv.Cube(), "sphere": pv.Sphere(center=(2, 2, 0))}
blocks = pv.MultiBlock(data)
blocks.keys()
# Expected:
## ['cube', 'sphere']
