# First, plot the unwarped mesh.
#
from pyvista import examples
mesh = examples.download_st_helens()
mesh.plot(cmap='gist_earth', show_scalar_bar=False)
#
# Now, warp the mesh by the ``'Elevation'`` scalars.
#
warped = mesh.warp_by_scalar('Elevation')
warped.plot(cmap='gist_earth', show_scalar_bar=False)
