# Save a mesh as a STL.
#
import pyvista
sphere = pyvista.Sphere()
sphere.save('my_mesh.stl')  # doctest:+SKIP
#
# Save a mesh as a PLY.
#
sphere = pyvista.Sphere()
sphere.save('my_mesh.ply')  # doctest:+SKIP
#
# Save a mesh as a PLY with a texture array.  Here we also
# create a simple RGB array representing the texture.
#
import numpy as np
sphere = pyvista.Sphere()
texture = np.zeros((sphere.n_points, 3), np.uint8)
texture[:, 1] = np.arange(sphere.n_points)[::-1]  # just blue channel
sphere.point_data['my_texture'] = texture
sphere.save('my_mesh.ply', texture='my_texture')  # doctest:+SKIP
#
# Alternatively, provide just the texture array.  This will be
# written to the file as ``'RGB'`` since it does not contain an
# alpha channel.
#
sphere.save('my_mesh.ply', texture=texture)  # doctest:+SKIP
#
# Save a mesh as a VTK file.
#
sphere = pyvista.Sphere()
sphere.save('my_mesh.vtk')  # doctest:+SKIP
