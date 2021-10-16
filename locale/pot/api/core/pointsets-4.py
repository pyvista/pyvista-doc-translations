# Load module and example file
import pyvista as pv
from pyvista import examples
import numpy as np

# Load example beam grid
grid = pv.UnstructuredGrid(examples.hexbeamfile)

# Create fictitious displacements as a function of Z location
d = np.zeros_like(grid.points)
d[:, 1] = grid.points[:, 2]**3/250

# use hardcoded camera position
cpos = [(11.915, 6.114, 3.612),
        (0.0, 0.375, 2.0),
        (-0.425, 0.902, -0.0679)]

plotter = pv.Plotter(window_size=(800, 600))
plotter.add_mesh(grid, scalars=d[:, 1],
                 scalar_bar_args={'title': 'Y Displacement'},
                 show_edges=True, rng=[-d.max(), d.max()],
                 interpolate_before_map=True)
plotter.add_axes()
plotter.camera_position = cpos

# open movie file.  A mp4 file can be written instead.  Requires ``moviepy``
plotter.open_gif('beam.gif')  # or beam.mp4

# Modify position of the beam cyclically
pts = grid.points.copy()  # unmodified points
for phase in np.linspace(0, 2*np.pi, 20):
    plotter.update_coordinates(pts + d*np.cos(phase))
    plotter.update_scalars(d[:, 1]*np.cos(phase))
    plotter.write_frame()

# close the plotter when complete
plotter.close()