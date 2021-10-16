# Create a sphere and translate it by ``(2, 1, 2)``.
#
import pyvista
mesh = pyvista.Sphere()
mesh.center
# Expected:
## [0.0, 0.0, 0.0]
mesh.translate((2, 1, 2))
mesh.center
# Expected:
## [2.0, 1.0, 2.0]
