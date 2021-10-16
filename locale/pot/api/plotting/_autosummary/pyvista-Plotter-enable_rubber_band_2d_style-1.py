# Create a simple scene with a plotter that has the Rubber Band
# 2D interactive style:
#
import pyvista as pv
plotter = pv.Plotter()
_ = plotter.add_mesh(pv.Cube(center=(1, 0, 0)))
_ = plotter.add_mesh(pv.Cube(center=(0, 1, 0)))
plotter.show_axes()
plotter.enable_rubber_band_2d_style()
plotter.show()  # doctest:+SKIP
