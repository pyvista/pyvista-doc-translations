# Plot evenly spaced streamlines for cylinder in a crossflow.
# This dataset is a multiblock dataset, and the fluid velocity is in the
# first block.
#
import pyvista
from pyvista import examples
mesh = examples.download_cylinder_crossflow()
streams = mesh[0].streamlines_evenly_spaced_2D(start_position=(4, 0.1, 0.),
                                               separating_distance=3,
                                               separating_distance_ratio=0.2)
plotter = pyvista.Plotter()
_ = plotter.add_mesh(streams.tube(radius=0.02), scalars="vorticity_mag")
plotter.view_xy()
plotter.show()
