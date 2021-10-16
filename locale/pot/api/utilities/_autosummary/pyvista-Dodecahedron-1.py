# Create and plot a dodecahedron.
#
import pyvista
tetra = pyvista.Dodecahedron()
tetra.plot(categories=True)
