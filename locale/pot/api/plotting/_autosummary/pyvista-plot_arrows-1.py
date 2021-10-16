# Plot a single random arrow.
#
import numpy as np
import pyvista
cent = np.random.random(3)
direction = np.random.random(3)
pyvista.plot_arrows(cent, direction)
#
# Plot 100 random arrows.
#
import numpy as np
import pyvista
cent = np.random.random((100, 3))
direction = np.random.random((100, 3))
pyvista.plot_arrows(cent, direction)
