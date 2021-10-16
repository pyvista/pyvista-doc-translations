# Set both the position and view of the camera.
#
import pyvista
pyvista.global_theme.camera = {'position': [1, 1, 1],
                               'viewup': [0, 0, 1]}
#
# Set the default position of the camera.
#
pyvista.global_theme.camera['position'] = [1, 1, 1]
#
# Set the default view of the camera.
#
pyvista.global_theme.camera['viewup'] = [0, 0, 1]
