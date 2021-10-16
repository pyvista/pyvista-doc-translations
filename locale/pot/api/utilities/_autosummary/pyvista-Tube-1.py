# Create a tube between ``(0, 0, 0)`` and ``(0, 0, 1)``.
#
import pyvista
mesh = pyvista.Tube((0, 0, 0), (0, 0, 1))
mesh.plot()
