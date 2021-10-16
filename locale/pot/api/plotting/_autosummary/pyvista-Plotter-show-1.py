# Simply show the plot of a mesh.
#
import pyvista as pv
pl = pv.Plotter()
_ = pl.add_mesh(pv.Cube())
pl.show()
#
# Take a screenshot interactively.  Screenshot will be of the
# first image shown, so use the first call with
# ``auto_close=False`` to set the scene before taking the
# screenshot.
#
pl = pv.Plotter()
_ = pl.add_mesh(pv.Cube())
pl.show(auto_close=False)  # doctest:+SKIP
pl.show(screenshot='my_image.png')  # doctest:+SKIP
#
# Display a ``pythreejs`` scene within a jupyter notebook
#
pl.show(jupyter_backend='pythreejs')  # doctest:+SKIP
#
# Return a ``pythreejs`` scene.
#
pl.show(jupyter_backend='pythreejs', return_viewer=True)  # doctest:+SKIP
#
# Obtain the camera position when using ``show``.
#
pl = pv.Plotter()
_ = pl.add_mesh(pv.Sphere())
pl.show(return_cpos=True)   # doctest:+SKIP
# Expected:
## [(2.223005211686484, -0.3126909484828709, 2.4686209867735065),
## (0.0, 0.0, 0.0),
## (-0.6839951597283509, -0.47207319712073137, 0.5561452310578585)]
