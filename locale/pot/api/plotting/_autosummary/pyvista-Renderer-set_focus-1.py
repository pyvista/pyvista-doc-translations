import pyvista
mesh = pyvista.Cube()
pl = pyvista.Plotter()
_ = pl.add_mesh(mesh, show_edges=True)
_ = pl.add_point_labels([mesh.points[1]], ["Focus"])
_ = pl.camera  # this initializes the camera
pl.set_focus(mesh.points[1])
pl.show()
