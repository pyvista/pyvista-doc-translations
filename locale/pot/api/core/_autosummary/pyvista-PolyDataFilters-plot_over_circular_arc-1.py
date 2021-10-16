# Sample a dataset along a high resolution circular arc and plot.
#
from pyvista import examples
mesh = examples.load_uniform()
a = [mesh.bounds[0], mesh.bounds[2], mesh.bounds[5]]
b = [mesh.bounds[1], mesh.bounds[2], mesh.bounds[4]]
center = [mesh.bounds[0], mesh.bounds[2], mesh.bounds[4]]
mesh.plot_over_circular_arc(a, b, center, resolution=1000, show=False)  # doctest:+SKIP
