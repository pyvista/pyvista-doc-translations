import pyvista
pl = pyvista.Plotter()
pl.camera.position
# Expected:
## (1.0, 1.0, 1.0)
pl.camera.position = (2.0, 1.0, 1.0)
pl.camera.position
# Expected:
## (2.0, 1.0, 1.0)
