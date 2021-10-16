# Quarter arc centered at the origin in the xy plane.
#
import pyvista
normal = [0, 0, 1]
polar = [-1, 0, 0]
arc = pyvista.CircularArcFromNormal([0, 0, 0], normal=normal, polar=polar)
pl = pyvista.Plotter()
_ = pl.add_mesh(arc, color='k', line_width=10)
_ = pl.show_bounds(location='all', font_size=30, use_2d=True)
_ = pl.view_xy()
pl.show()
