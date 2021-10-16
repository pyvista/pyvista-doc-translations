# Create and plot an icosahedron.
#
import pyvista
tetra = pyvista.Icosahedron()
tetra.plot(categories=True)
