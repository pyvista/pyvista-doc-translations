# Create a box with subdivision ``level=2``.
#
import pyvista
mesh = pyvista.Box(level=2)
mesh.plot(show_edges=True)
