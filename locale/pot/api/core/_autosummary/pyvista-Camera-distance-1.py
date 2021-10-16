import pyvista
pl = pyvista.Plotter()
pl.camera.distance
# Expected:
## 1.73205
pl.camera.distance = 2.0
pl.camera.distance
# Expected:
## 2.0
