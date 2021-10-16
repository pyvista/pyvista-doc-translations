import pyvista
from pyvista import examples
plotter = pyvista.Plotter()
actor = plotter.add_mesh(pyvista.Sphere())
plotter.add_background_image(examples.mapfile)
plotter.show()
