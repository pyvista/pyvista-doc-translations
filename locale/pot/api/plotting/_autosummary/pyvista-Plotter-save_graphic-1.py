import pyvista
from pyvista import examples
pl = pyvista.Plotter()
_ = pl.add_mesh(examples.load_airplane(), smooth_shading=True)
_ = pl.add_background_image(examples.mapfile)
pl.save_graphic("img.svg")  # doctest:+SKIP
