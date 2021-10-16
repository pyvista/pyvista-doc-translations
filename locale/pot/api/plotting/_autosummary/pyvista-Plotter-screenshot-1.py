import pyvista
sphere = pyvista.Sphere()
plotter = pyvista.Plotter(off_screen=True)
actor = plotter.add_mesh(sphere)
plotter.screenshot('screenshot.png')  # doctest:+SKIP
