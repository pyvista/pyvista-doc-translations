import numpy as np
import pyvista as pv
ni, nj, nk = 4, 5, 6
si, sj, sk = 20, 10, 1
grid_ijk = np.mgrid[:(ni+1)*si:si, :(nj+1)*sj:sj, :(nk+1)*sk:sk]
for axis in range(1, 4):
    grid_ijk = grid_ijk.repeat(2, axis=axis)
grid_ijk = grid_ijk[:, 1:-1, 1:-1, 1:-1]
corners = grid_ijk.transpose().reshape(-1, 3)
dims = np.array([ni, nj, nk]) + 1
grid = pv.ExplicitStructuredGrid(dims, corners)
_ = grid.compute_connectivity()
grid.plot(show_edges=True)  # doctest:+SKIP
