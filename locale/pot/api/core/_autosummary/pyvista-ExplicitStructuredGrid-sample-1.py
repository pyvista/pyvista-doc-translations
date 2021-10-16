# Resample data from another dataset onto a sphere.
#
import pyvista
from pyvista import examples
mesh = pyvista.Sphere(center=(4.5, 4.5, 4.5), radius=4.5)
data_to_probe = examples.load_uniform()
result = mesh.sample(data_to_probe)
result.plot(scalars="Spatial Point Data")
