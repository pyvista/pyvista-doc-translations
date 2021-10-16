# Plot a random field of vectors and save a screenshot of it.
#
import numpy as np
import pyvista
cent = np.random.random((10, 3))
direction = np.random.random((10, 3))
plotter = pyvista.Plotter()
_ = plotter.add_arrows(cent, direction, mag=2)
plotter.show()
