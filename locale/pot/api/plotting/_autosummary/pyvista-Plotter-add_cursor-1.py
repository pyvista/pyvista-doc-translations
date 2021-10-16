import pyvista
sphere = pyvista.Sphere()
plotter = pyvista.Plotter()
_ = plotter.add_mesh(sphere)
_ = plotter.add_cursor()
plotter.show()
