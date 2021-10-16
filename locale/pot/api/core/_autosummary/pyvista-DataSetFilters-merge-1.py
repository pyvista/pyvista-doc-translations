# Merge three separate spheres into a single mesh.
#
import pyvista
sphere_a = pyvista.Sphere(center=(1, 0, 0))
sphere_b = pyvista.Sphere(center=(0, 1, 0))
sphere_c = pyvista.Sphere(center=(0, 0, 1))
merged = sphere_a.merge([sphere_b, sphere_c])
merged.plot()
