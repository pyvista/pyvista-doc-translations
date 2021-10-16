# Join two meshes together, extract the largest, and plot it.
#
import pyvista
mesh = pyvista.Sphere() + pyvista.Cube()
largest = mesh.extract_largest()
largest.point_data.clear()
largest.cell_data.clear()
largest.plot()
