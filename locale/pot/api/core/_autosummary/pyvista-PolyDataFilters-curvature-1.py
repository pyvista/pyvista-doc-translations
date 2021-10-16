# Calculate the mean curvature of the hills example mesh.
#
from pyvista import examples
hills = examples.load_random_hills()
curv = hills.curvature()
curv   # doctest:+SKIP
# Expected:
## array([0.20587616, 0.06747695, ..., 0.11781171, 0.15988467])
#
# Plot it.
#
hills.plot(scalars=curv)
