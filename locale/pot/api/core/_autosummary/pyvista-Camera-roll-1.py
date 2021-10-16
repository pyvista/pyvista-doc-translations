import pyvista
pl = pyvista.Plotter()
pl.camera.roll
# Expected:
## -120.00000000000001
pl.camera.roll = 45.0
pl.camera.roll
# Expected:
## 45.0
