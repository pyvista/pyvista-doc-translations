import pyvista
mesh = pyvista.Sphere()
pl = pyvista.Plotter()
_ = pl.add_mesh(mesh, label='sphere')
_ = pl.add_legend()
pl.remove_legend()
