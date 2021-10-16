# Split a uniform grid thresholded to be non-connected.
#
from pyvista import examples
dataset = examples.load_uniform()
dataset.set_active_scalars('Spatial Cell Data')
threshed = dataset.threshold_percent([0.15, 0.50], invert=True)
bodies = threshed.split_bodies()
len(bodies)
# Expected:
## 2
