# Create a quarter arc centered at the origin in the xy plane.
#
import pyvista
arc = pyvista.CircularArc([-1, 0, 0], [0, 1, 0], [0, 0, 0])
pl = pyvista.Plotter()
_ = pl.add_mesh(arc, color='k', line_width=10)
_ = pl.show_bounds(location='all', font_size=30, use_2d=True)
_ = pl.view_xy()
pl.show()
