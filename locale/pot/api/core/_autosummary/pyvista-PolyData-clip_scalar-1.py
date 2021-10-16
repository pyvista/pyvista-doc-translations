# Remove the part of the mesh with "sample_point_scalars" above 100.
#
import pyvista as pv
from pyvista import examples
dataset = examples.load_hexbeam()
clipped = dataset.clip_scalar(scalars="sample_point_scalars", value=100)
clipped.plot()
#
# Get clipped meshes corresponding to the portions of the mesh above and below 100.
#
import pyvista as pv
from pyvista import examples
dataset = examples.load_hexbeam()
_below, _above = dataset.clip_scalar(scalars="sample_point_scalars", value=100, both=True)
#
# Remove the part of the mesh with "sample_point_scalars" below 100.
#
import pyvista as pv
from pyvista import examples
dataset = examples.load_hexbeam()
clipped = dataset.clip_scalar(scalars="sample_point_scalars", value=100, invert=False)
clipped.plot()
