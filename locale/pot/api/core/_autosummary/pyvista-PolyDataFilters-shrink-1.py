# First, plot the original cube.
#
import pyvista
mesh = pyvista.Cube()
mesh.plot(show_edges=True, line_width=5)
#
# Now, plot the mesh with shrunk faces.
#
shrunk = mesh.shrink(0.5)
shrunk.clear_data()  # cleans up plot
shrunk.plot(show_edges=True, line_width=5)
