# Generate an orbital path around a sphere.
#
import pyvista
plotter = pyvista.Plotter()
_ = plotter.add_mesh(pyvista.Sphere())
viewup = [0, 0, 1]
orbit = plotter.generate_orbital_path(factor=2.0, n_points=50,
                                      shift=0.0, viewup=viewup)
