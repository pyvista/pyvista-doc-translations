# Move the camera far away to ``[7, 7, 7]``.
#
import pyvista
mesh = pyvista.Cube()
pl = pyvista.Plotter()
_ = pl.add_mesh(mesh, show_edges=True)
pl.set_position([7, 7, 7])
pl.show()
