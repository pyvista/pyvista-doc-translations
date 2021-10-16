import pyvista
from pyvista import examples
pl = pyvista.Plotter()
_ = pl.add_mesh(examples.load_hexbeam())
pl.export_vtkjs("sample")  # doctest:+SKIP
