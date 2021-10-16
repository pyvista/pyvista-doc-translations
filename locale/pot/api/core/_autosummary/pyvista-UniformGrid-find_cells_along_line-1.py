import pyvista
mesh = pyvista.Sphere()
index = mesh.find_cells_along_line([0, 0, 0], [0, 0, 1.0])
