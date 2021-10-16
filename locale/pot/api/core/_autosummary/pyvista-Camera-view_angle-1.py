import pyvista
plotter = pyvista.Plotter()
plotter.camera.view_angle
# Expected:
## 30.0
plotter.camera.view_angle = 60.0
plotter.camera.view_angle
# Expected:
## 60.0
