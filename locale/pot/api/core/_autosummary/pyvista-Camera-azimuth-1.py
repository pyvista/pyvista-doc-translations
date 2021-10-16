import pyvista
pl = pyvista.Plotter()
pl.camera.azimuth
# Expected:
## 0.0
pl.camera.azimuth = 45.0
pl.camera.azimuth
# Expected:
## 45.0
