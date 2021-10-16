import pyvista
pl = pyvista.Plotter()
pl.camera.focal_point
# Expected:
## (0.0, 0.0, 0.0)
pl.camera.focal_point = (2.0, 0.0, 0.0)
pl.camera.focal_point
# Expected:
## (2.0, 0.0, 0.0)
