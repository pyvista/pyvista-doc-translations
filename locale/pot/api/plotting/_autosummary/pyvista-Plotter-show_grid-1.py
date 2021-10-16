import pyvista
from pyvista import examples
pl = pyvista.Plotter()
_ = pl.add_mesh(examples.download_guitar())
_ = pl.show_grid()
pl.show()
