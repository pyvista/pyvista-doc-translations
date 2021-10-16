import pyvista as pv
#
# Create empty composite dataset
#
blocks = pv.MultiBlock()
#
# Add a dataset to the collection.
#
sphere = pv.Sphere()
blocks.append(sphere)
#
# Add a named block.
#
blocks["cube"] = pv.Cube()
#
# Instantiate from a list of objects.
#
data = [pv.Sphere(center=(2, 0, 0)), pv.Cube(center=(0, 2, 0)), 
        pv.Cone()]
blocks = pv.MultiBlock(data)
blocks.plot()
#
# Instantiate from a dictionary.
#
data = {"cube": pv.Cube(), "sphere": pv.Sphere(center=(2, 2, 0))}
blocks = pv.MultiBlock(data)
blocks.plot()
#
# Iterate over the collection
#
for name in blocks.keys():
    block = blocks[name]
#
for block in blocks:
    surf = block.extract_surface()  # Do something with each dataset
