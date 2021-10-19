# Enable stereo rendering to show a cube as an anaglyph image.
#
import pyvista as pv
pl = pv.Plotter()
_ = pl.add_mesh(pv.Cube())
pl.enable_stereo_render()
pl.show()
