import pyvista
plotter = pyvista.Plotter()
actor = plotter.add_mesh(pyvista.Sphere())
plotter.clear()
plotter.renderer.actors
# Expected:
## {}
