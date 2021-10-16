# Sample a dataset along a high resolution circular arc and plot.
#
from pyvista import examples
mesh = examples.load_uniform()
normal = normal = [0, 0, 1]
polar = [0, 9, 0]
angle = 90
center = [mesh.bounds[0], mesh.bounds[2], mesh.bounds[4]]
mesh.plot_over_circular_arc_normal(center, polar=polar, angle=angle)  # doctest:+SKIP
