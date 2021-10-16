# Plot a simple sphere while showing its edges.
#
import pyvista
mesh = pyvista.Sphere()
mesh.plot(show_edges=True)
