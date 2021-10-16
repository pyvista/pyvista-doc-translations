# Create empty composite dataset
#
import pyvista
blocks = pyvista.MultiBlock()
#
# Add a dataset to the collection
#
blocks.append(pyvista.Sphere())
#
# Or add a named block
#
blocks["cube"] = pyvista.Cube(center=(0, 0, -1))
#
# Plotting the MultiBlock plots all the meshes contained by it.
#
blocks.plot(smooth_shading=True)
