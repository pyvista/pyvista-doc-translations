# Slice the random hills dataset with three orthogonal planes.
#
from pyvista import examples
hills = examples.load_random_hills()
slices = hills.slice_orthogonal(contour=False)
slices.plot(line_width=5)
