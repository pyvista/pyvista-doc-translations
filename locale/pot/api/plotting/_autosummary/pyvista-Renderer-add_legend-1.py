# Create a legend by labeling the meshes when using ``add_mesh``
#
import pyvista
from pyvista import examples
sphere = pyvista.Sphere(center=(0, 0, 1))
cube = pyvista.Cube()
plotter = pyvista.Plotter()
_ = plotter.add_mesh(sphere, 'grey', smooth_shading=True, label='Sphere')
_ = plotter.add_mesh(cube, 'r', label='Cube')
_ = plotter.add_legend(bcolor='w', face=None)
plotter.show()
#
# Alternatively provide labels in the plotter.
#
plotter = pyvista.Plotter()
_ = plotter.add_mesh(sphere, 'grey', smooth_shading=True)
_ = plotter.add_mesh(cube, 'r')
legend_entries = []
legend_entries.append(['My Mesh', 'w'])
legend_entries.append(['My Other Mesh', 'k'])
_ = plotter.add_legend(legend_entries)
plotter.show()
