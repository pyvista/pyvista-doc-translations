# Extract all the points of a sphere with a Z coordinate greater than 0
#
import pyvista
sphere = pyvista.Sphere()
extracted = sphere.extract_points(sphere.points[:, 2] > 0)
extracted.clear_data()  # clear for plotting
extracted.plot()
