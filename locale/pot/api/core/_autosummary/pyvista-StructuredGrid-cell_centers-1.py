import pyvista
mesh = pyvista.Plane()
mesh.point_data.clear()
centers = mesh.cell_centers()
pl = pyvista.Plotter()
actor = pl.add_mesh(mesh, show_edges=True)
actor = pl.add_points(centers, render_points_as_spheres=True,
                      color='red', point_size=20)
pl.show()
