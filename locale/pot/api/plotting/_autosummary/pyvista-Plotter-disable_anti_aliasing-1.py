import pyvista
pl = pyvista.Plotter()
pl.disable_anti_aliasing()
_ = pl.add_mesh(pyvista.Sphere(), show_edges=True)
pl.show()
