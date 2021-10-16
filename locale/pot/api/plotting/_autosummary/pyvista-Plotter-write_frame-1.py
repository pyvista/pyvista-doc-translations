import pyvista
plotter = pyvista.Plotter()
plotter.open_movie(filename)  # doctest:+SKIP
plotter.add_mesh(pyvista.Sphere())  # doctest:+SKIP
plotter.write_frame()  # doctest:+SKIP
