import pyvista
from pyvista import examples
bunny = examples.download_bunny()
plotter = pyvista.Plotter()
_ = plotter.add_mesh(bunny, color='tan')
_ = plotter.add_silhouette(bunny,
    params={'color': 'red', 'line_width': 8.0})
plotter.view_xy()
plotter.show()
