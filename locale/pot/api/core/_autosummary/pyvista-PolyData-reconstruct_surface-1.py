# Create a point cloud out of a sphere and reconstruct a surface
# from it.
#
import pyvista as pv
points = pv.wrap(pv.Sphere().points)
surf = points.reconstruct_surface()
#
pl = pv.Plotter(shape=(1,2))
_ = pl.add_mesh(points)
_ = pl.add_title('Point Cloud of 3D Surface')
pl.subplot(0,1)
_ = pl.add_mesh(surf, color=True, show_edges=True)
_ = pl.add_title('Reconstructed Surface')
pl.show()
#
# See :ref:`surface_reconstruction_example` for more examples
