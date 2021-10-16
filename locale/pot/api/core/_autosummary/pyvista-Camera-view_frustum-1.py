import pyvista
plotter = pyvista.Plotter()
frustum = plotter.camera.view_frustum(1.0)
frustum.n_points
# Expected:
## 8
frustum.n_cells
# Expected:
## 6
