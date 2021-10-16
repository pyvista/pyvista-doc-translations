import pyvista
from pyvista import demos
pl = demos.orientation_plotter()
pl.camera_position = 'yz'
pl.camera.roll += 10
pl.show()