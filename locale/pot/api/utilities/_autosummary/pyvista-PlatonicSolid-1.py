# Create and plot a dodecahedron.
#
import pyvista
dodeca = pyvista.PlatonicSolid('dodecahedron')
dodeca.plot(categories=True)
