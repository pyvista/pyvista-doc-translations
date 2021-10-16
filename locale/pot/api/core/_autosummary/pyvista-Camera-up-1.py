import pyvista
pl = pyvista.Plotter()
pl.camera.up
# Expected:
## (0.0, 0.0, 1.0)
pl.camera.up = (0.410018, 0.217989, 0.885644)
pl.camera.up
# Expected:
## (0.410018, 0.217989, 0.885644)
