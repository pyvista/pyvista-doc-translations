import pyvista
wavelet = pyvista.Wavelet(extent=(0, 50, 0, 50, 0, 10), x_freq=20,
                          y_freq=10, z_freq=1, x_mag=100, y_mag=100, 
                          z_mag=1000)
wavelet.plot(show_scalar_bar=False)
#
# Extract lower valued cells of the wavelet and create a surface from it.
#
thresh = wavelet.threshold(800).extract_surface()
thresh.plot(show_scalar_bar=False)
#
# Smooth it to create "waves"
#
waves = thresh.smooth(n_iter=100, relaxation_factor=0.1)
waves.plot(color='white', smooth_shading=True, show_edges=True)
