# Load module and example file
import pyvista as pv
from pyvista import examples

# Load example beam file
grid = pv.UnstructuredGrid(examples.hexbeamfile)

# Create plotting class and add the unstructured grid
plotter = pv.Plotter()
plotter.add_mesh(grid, show_edges=True, color='tan')

# Add labels to points on the yz plane (where x == 0)
points = grid.points
mask = points[:, 0] == 0
plotter.add_point_labels(points[mask], points[mask].tolist())

plotter.camera_position = [
                (-1.4643015810492384, 1.5603923627830638, 3.16318236536270),
                (0.05268120500967251, 0.639442034364944, 1.204095304165153),
                (0.2364061044392675, 0.9369426029156169, -0.25739213784721)]

plotter.show()