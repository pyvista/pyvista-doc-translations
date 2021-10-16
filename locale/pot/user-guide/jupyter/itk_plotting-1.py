import pyvista
mesh = pyvista.Sphere()
pl = pyvista.PlotterITK()  # doctest:+SKIP
pl.add_mesh(mesh, color='w')  # doctest:+SKIP
pl.background_color = 'k'  # doctest:+SKIP
pl.show()  # doctest:+SKIP
