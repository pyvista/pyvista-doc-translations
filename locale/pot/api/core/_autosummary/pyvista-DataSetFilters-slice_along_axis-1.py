# Slice the random hills dataset in the X direction.
#
from pyvista import examples
hills = examples.load_random_hills()
slices = hills.slice_along_axis(n=10)
slices.plot(line_width=5)
#
# Slice the random hills dataset in the Z direction.
#
from pyvista import examples
hills = examples.load_random_hills()
slices = hills.slice_along_axis(n=10, axis='z')
slices.plot(line_width=5)
