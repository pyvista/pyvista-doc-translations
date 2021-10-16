# Smooth the edges of an all triangular cube
#
import pyvista as pv
cube = pv.Cube().triangulate().subdivide(5)
smooth_cube = cube.smooth(1000, feature_smoothing=False)
n_edge_cells = cube.extract_feature_edges().n_cells
n_smooth_cells = smooth_cube.extract_feature_edges().n_cells
f'Sharp Edges on Cube:        {n_edge_cells}'
# Expected:
## 'Sharp Edges on Cube:        384'
f'Sharp Edges on Smooth Cube: {n_smooth_cells}'
# Expected:
## 'Sharp Edges on Smooth Cube: 12'
smooth_cube.plot()
