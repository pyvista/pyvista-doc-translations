# Catch VTK errors using the context manager.
#
import pyvista
with pyvista.VtkErrorCatcher() as error_catcher:
    sphere = pyvista.Sphere()
