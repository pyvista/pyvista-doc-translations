# Apply a 50% threshold filter.
#
import pyvista
noise = pyvista.perlin_noise(0.1, (2, 2, 2), (0, 0, 0))
grid = pyvista.sample_function(noise, [0, 1.0, -0, 1.0, 0, 1.0],
                               dim=(30, 30, 30))
threshed = grid.threshold_percent(0.5)
threshed.plot(cmap='gist_earth_r', show_scalar_bar=False, show_edges=True)
#
# Apply a 80% threshold filter.
#
threshed = grid.threshold_percent(0.8)
threshed.plot(cmap='gist_earth_r', show_scalar_bar=False, show_edges=True)
