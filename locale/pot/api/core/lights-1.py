import pyvista as pv
from pyvista import examples
light = pv.Light(position=(-1, 1, 1), color='red')
light.positional = True

import pyvista as pv
from pyvista import examples
plotter = pv.Plotter(lighting='none')
plotter.background_color = 'white'
mesh = examples.download_bunny()
mesh.rotate_x(90)
mesh.rotate_z(180)
plotter.add_mesh(mesh, specular=1.0, diffuse=0.7, smooth_shading=True)
plotter.add_light(light)
plotter.show()