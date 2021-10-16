import pyvista
mesh = pyvista.Sphere(center=(1, 1, 1))
mesh.center_of_mass()
# Expected:
## array([1., 1., 1.])
