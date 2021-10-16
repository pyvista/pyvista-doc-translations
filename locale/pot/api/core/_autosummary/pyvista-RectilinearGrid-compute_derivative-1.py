# First, plot the random hills dataset with the active elevation
# scalars.  These scalars will be used for the derivative
# calculations.
#
from pyvista import examples
hills = examples.load_random_hills()
hills.plot(smooth_shading=True)
#
# Compute and plot the gradient of the active scalars.
#
from pyvista import examples
hills = examples.load_random_hills()
deriv = hills.compute_derivative()
deriv.plot(scalars='gradient')
