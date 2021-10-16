import pyvista as pv
data = {"cube": pv.Cube(), "sphere": pv.Sphere(center=(2, 2, 0))}
blocks = pv.MultiBlock(data)
blocks.get_index_by_name('sphere')
# Expected:
## 1
