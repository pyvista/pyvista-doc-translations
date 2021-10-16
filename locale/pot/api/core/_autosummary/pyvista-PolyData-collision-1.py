# Compute the collision between a sphere and the back faces of a
# cube and output the cell indices of the first 10 collisions.
#
import numpy as np
import pyvista
mesh_a = pyvista.Sphere(radius=0.5)
mesh_b = pyvista.Cube((0.5, 0.5, 0.5)).extract_cells([0, 2, 4])
collision, ncol = mesh_a.collision(mesh_b, cell_tolerance=1)
collision['ContactCells'][:10]
# Expected:
## array([471, 471, 468, 468, 469, 469, 466, 466, 467, 467])
#
# Plot the collisions by creating a collision mask with the
# ``"ContactCells"`` field data.  Cells with a collision are
# colored red.
#
scalars = np.zeros(collision.n_cells, dtype=bool)
scalars[collision.field_data['ContactCells']] = True
pl = pyvista.Plotter()
_ = pl.add_mesh(collision, scalars=scalars, show_scalar_bar=False,
                cmap='bwr')
_ = pl.add_mesh(mesh_b, color='tan', line_width=5, opacity=0.7,
                show_edges=True)
pl.show()
#
# Alternatively, simply plot the collisions using the default
# ``'collision_rgba'`` array after enabling ``generate_scalars``.
#
collision, ncol = mesh_a.collision(mesh_b, cell_tolerance=1,
                                   generate_scalars=True)
collision.plot()
