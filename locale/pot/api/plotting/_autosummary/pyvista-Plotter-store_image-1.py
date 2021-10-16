import pyvista
pl = pyvista.Plotter(off_screen=True)
pl.store_image = True
_ = pl.add_mesh(pyvista.Cube())
pl.show()
image = pl.last_image
type(image)  # doctest:+SKIP
# Expected:
## <class 'numpy.ndarray'>
