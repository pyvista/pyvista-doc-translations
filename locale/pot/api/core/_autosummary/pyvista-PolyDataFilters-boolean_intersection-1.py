# Demonstrate a boolean intersection with two spheres.  Note how
# the final mesh only includes the intersection of the two.
#
import pyvista
sphere_a = pyvista.Sphere()
sphere_b = pyvista.Sphere(center=(0.5, 0, 0))
result = sphere_a.boolean_intersection(sphere_b)
pl = pyvista.Plotter()
_ = pl.add_mesh(sphere_a, color='r', style='wireframe', line_width=3)
_ = pl.add_mesh(sphere_b, color='b', style='wireframe', line_width=3)
_ = pl.add_mesh(result, color='tan')
pl.camera_position = 'xz'
pl.show()
