# Join two meshes together and plot their connectivity.
#
import pyvista
mesh = pyvista.Sphere() + pyvista.Sphere(center=(2, 0, 0))
conn = mesh.connectivity(largest=False)
conn.plot(cmap=['red', 'blue'])
