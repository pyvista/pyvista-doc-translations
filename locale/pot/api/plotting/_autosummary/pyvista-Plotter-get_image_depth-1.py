import pyvista
plotter = pyvista.Plotter()
actor = plotter.add_mesh(pyvista.Sphere())
plotter.store_image = True
plotter.show()
zval = plotter.get_image_depth()
