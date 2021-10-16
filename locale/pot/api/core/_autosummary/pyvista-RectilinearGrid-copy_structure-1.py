import pyvista as pv
source = pv.UniformGrid((10, 10, 5))
target = pv.UniformGrid()
target.copy_structure(source)
target.plot(show_edges=True)
