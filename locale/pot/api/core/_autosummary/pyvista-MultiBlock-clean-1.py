import pyvista as pv
data = {"cube": pv.Cube(), "empty": pv.PolyData()}
blocks = pv.MultiBlock(data)
blocks.clean(empty=True)
blocks.keys()
# Expected:
## ['cube']
