# Clear all point arrays from a mesh.
#
import pyvista
import numpy as np
mesh = pyvista.Sphere()
mesh.point_data.keys()
# Expected:
## ['Normals']
mesh.clear_point_data()
mesh.point_data.keys()
# Expected:
## []
