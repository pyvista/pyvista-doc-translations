# Create a cube and return the bounds of the mesh.
#
import pyvista
cube = pyvista.Cube()
cube.bounds
# Expected:
## [-0.5, 0.5, -0.5, 0.5, -0.5, 0.5]
