# Compare two active plotters.
#
import pyvista
pl1 = pyvista.Plotter()
_ = pl1.add_mesh(pyvista.Sphere(), smooth_shading=True)
pl2 = pyvista.Plotter()
_ = pl2.add_mesh(pyvista.Sphere(), smooth_shading=False)
error = pyvista.compare_images(pl1, pl2)
#
# Compare images from file.
#
import pyvista
img1 = pyvista.read('img1.png')  # doctest:+SKIP
img2 = pyvista.read('img2.png')  # doctest:+SKIP
pyvista.compare_images(img1, img2)  # doctest:+SKIP
