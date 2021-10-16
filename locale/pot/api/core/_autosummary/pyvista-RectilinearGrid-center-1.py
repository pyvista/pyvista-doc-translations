# Get the center of a mesh.
#
import pyvista
mesh = pyvista.Sphere(center=(1, 2, 0))
mesh.center
# Expected:
## [1.0, 2.0, 0.0]
