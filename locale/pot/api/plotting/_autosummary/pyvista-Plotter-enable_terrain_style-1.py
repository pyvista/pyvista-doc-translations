# Create a simple scene with a plotter that has the Terrain
# interactive style:
#
import pyvista as pv
plotter = pv.Plotter()
_ = plotter.add_mesh(pv.Cube(center=(1, 0, 0)))
_ = plotter.add_mesh(pv.Cube(center=(0, 1, 0)))
plotter.show_axes()
plotter.enable_terrain_style()
plotter.show()  # doctest:+SKIP
#
# Use controls that are closer to the default style:
#
plotter = pv.Plotter()
_ = plotter.add_mesh(pv.Cube(center=(1, 0, 0)))
_ = plotter.add_mesh(pv.Cube(center=(0, 1, 0)))
plotter.show_axes()
plotter.enable_terrain_style(mouse_wheel_zooms=True,
                             shift_pans=True)
plotter.show()  # doctest:+SKIP
