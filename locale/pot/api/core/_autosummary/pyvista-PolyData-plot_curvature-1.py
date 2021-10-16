# Plot the Gaussian curvature of an example mesh.  Override the
# default scalar bar range as the mesh edges report high
# curvature.
#
from pyvista import examples
hills = examples.load_random_hills()
hills.plot_curvature(curv_type='gaussian', smooth_shading=True, 
                     clim=[0, 1])
