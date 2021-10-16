# Generate contours for the random hills dataset.
#
from pyvista import examples
hills = examples.load_random_hills()
contours = hills.contour()
contours.plot(line_width=5)
