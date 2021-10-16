import pyvista
from pyvista import examples
mesh = examples.load_uniform()
pl = pyvista.Plotter(shape=(1,2))
_ = pl.add_mesh(mesh, scalars='Spatial Point Data', show_edges=True)
pl.subplot(0,1)
_ = pl.add_mesh(mesh, scalars='Spatial Cell Data', show_edges=True)
pl.export_html('pyvista.html')  # doctest:+SKIP
