# First compute the face area of the example airplane mesh and
# show the cell values.  This is to show discrete cell data.
#
from pyvista import examples
surf = examples.load_airplane()
surf = surf.compute_cell_sizes(length=False, volume=False)
surf.plot(smooth_shading=True)
#
# These cell scalars can be applied to individual points to
# effectively smooth out the cell data onto the points.
#
from pyvista import examples
surf = examples.load_airplane()
surf = surf.compute_cell_sizes(length=False, volume=False)
surf = surf.cell_data_to_point_data()
surf.plot(smooth_shading=True)
