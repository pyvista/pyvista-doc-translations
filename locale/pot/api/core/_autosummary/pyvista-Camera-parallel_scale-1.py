import pyvista
pl = pyvista.Plotter()
pl.camera.parallel_scale
# Expected:
## 1.0
pl.camera.parallel_scale = 2.0
pl.camera.parallel_scale
# Expected:
## 2.0
