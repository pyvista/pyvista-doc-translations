import pyvista
import numpy as np
volume = np.zeros([10, 10, 10])
volume[:3] = 1
vol = pyvista.wrap(volume)
threshed = vol.threshold(0.1)
threshed  # doctest:+SKIP
# Expected:
## UnstructuredGrid (0x7f00f9983fa0)
##   N Cells:      243
##   N Points:     400
##   X Bounds:     0.000e+00, 3.000e+00
##   Y Bounds:     0.000e+00, 9.000e+00
##   Z Bounds:     0.000e+00, 9.000e+00
##   N Arrays:     1
#
# Apply the threshold filter to Perlin noise.  First generate
# the structured grid.
#
import pyvista
noise = pyvista.perlin_noise(0.1, (1, 1, 1), (0, 0, 0))
grid = pyvista.sample_function(noise, [0, 1.0, -0, 1.0, 0, 1.0],
                               dim=(20, 20, 20))
grid.plot(cmap='gist_earth_r', show_scalar_bar=True, show_edges=False)
#
# Next, apply the threshold.
#
import pyvista
noise = pyvista.perlin_noise(0.1, (1, 1, 1), (0, 0, 0))
grid = pyvista.sample_function(noise, [0, 1.0, -0, 1.0, 0, 1.0],
                               dim=(20, 20, 20))
threshed = grid.threshold(value=0.02)
threshed.plot(cmap='gist_earth_r', show_scalar_bar=False, show_edges=True)
