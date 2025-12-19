import pyvista as pv
import numpy as np

def make_cube():
    x = np.linspace(-0.5, 0.5, 25)
    grid = pv.StructuredGrid(*np.meshgrid(x, x, x))
    surf = grid.extract_surface().triangulate().flip_faces()
    return surf

# Create example PolyData meshes for boolean operations
sphere = pv.Sphere(radius=0.65, center=(0, 0, 0))
cube = make_cube()

# Perform a boolean difference
boolean = cube.boolean_difference(sphere)
boolean.plot(color='darkgrey', smooth_shading=True, split_sharp_edges=True)