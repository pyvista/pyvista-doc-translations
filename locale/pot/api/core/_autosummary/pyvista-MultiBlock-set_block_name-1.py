import pyvista as pv
data = {"cube": pv.Cube(), "sphere": pv.Sphere(center=(2, 2, 0))}
blocks = pv.MultiBlock(data)
blocks.append(pv.Cone())
blocks.set_block_name(2, 'cone')
blocks.keys()
# Expected:
## ['cube', 'sphere', 'cone']
