import pyvista
pl = pyvista.Plotter()
_ = pl.add_mesh(pyvista.Sphere())
_ = pl.add_bounding_box(line_width=5, color='black')
pl.show()
