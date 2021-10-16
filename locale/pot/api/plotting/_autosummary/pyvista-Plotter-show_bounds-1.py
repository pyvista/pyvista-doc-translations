import pyvista
mesh = pyvista.Sphere()
plotter = pyvista.Plotter()
actor = plotter.add_mesh(mesh)
actor = plotter.show_bounds(grid='front', location='outer', 
                            all_edges=True)
plotter.show()
