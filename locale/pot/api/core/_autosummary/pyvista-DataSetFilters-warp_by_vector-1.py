# Warp a sphere by vectors.
#
import pyvista as pv
from pyvista import examples
sphere = examples.load_sphere_vectors()
warped = sphere.warp_by_vector()
pl = pv.Plotter(shape=(1, 2))
pl.subplot(0, 0)
actor = pl.add_text("Before warp")
actor = pl.add_mesh(sphere, color='white')
pl.subplot(0, 1)
actor = pl.add_text("After warp")
actor = pl.add_mesh(warped, color='white')
pl.show()
