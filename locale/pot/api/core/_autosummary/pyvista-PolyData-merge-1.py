import pyvista
sphere_a = pyvista.Sphere()
sphere_b = pyvista.Sphere(center=(0.5, 0, 0))
merged = sphere_a.merge(sphere_b)
merged.plot(style='wireframe', color='tan')
