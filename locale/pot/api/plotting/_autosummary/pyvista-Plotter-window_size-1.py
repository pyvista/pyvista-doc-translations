# Change the window size from ``200 x 200`` to ``400 x 400``.
#
import pyvista
pl = pyvista.Plotter(window_size=[200, 200])
pl.window_size
# Expected:
## [200, 200]
pl.window_size = [400, 400]
pl.window_size
# Expected:
## [400, 400]
