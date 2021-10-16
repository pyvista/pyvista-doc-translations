# Use an Arrow as the orientation widget.
#
import pyvista
pl = pyvista.Plotter()
actor = pl.add_mesh(pyvista.Cube(), show_edges=True)
actor = pl.add_orientation_widget(pyvista.Arrow(), color='r')
pl.show()
