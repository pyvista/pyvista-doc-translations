# Plot the turbine blade mesh.
#
from pyvista import examples
blade_mesh = examples.download_turbine_blade()
blade_mesh.plot()
