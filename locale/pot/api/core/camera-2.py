import pyvista
from pyvista import demos
pl = demos.orientation_plotter()
pl.camera_position = 'yz'
pl.show()