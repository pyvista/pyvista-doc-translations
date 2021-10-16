import pyvista
pl = pyvista.Plotter()
actor = pl.add_text('Sample Text', position='upper_right', color='blue',
                    shadow=True, font_size=26)
pl.show()
