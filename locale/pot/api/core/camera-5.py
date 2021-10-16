import pyvista
from pyvista import demos
pl = demos.orientation_plotter()
pl.camera_position = 'yz'
pl.camera.elevation = 45
pl.show()