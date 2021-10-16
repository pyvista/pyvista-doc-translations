import pyvista
pl = pyvista.Plotter()
pl.background_color = 'grey'
actor = pl.add_title('Plot Title', font='courier', color='k', 
                     font_size=40)
pl.show()
