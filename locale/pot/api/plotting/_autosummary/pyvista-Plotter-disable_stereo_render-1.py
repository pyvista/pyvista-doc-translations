# Enable and then disable stereo rendering. It should show a simple cube.
#
import pyvista as pv
pl = pv.Plotter()
_ = pl.add_mesh(pv.Cube())
pl.enable_stereo_render()
pl.disable_stereo_render()
pl.show()
