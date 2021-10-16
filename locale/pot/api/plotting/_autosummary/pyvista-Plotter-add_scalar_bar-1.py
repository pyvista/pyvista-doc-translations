# Add a custom interactive scalar bar that is horizontal, has an
# outline, and has a custom formatting.
#
import pyvista as pv
sphere = pv.Sphere()
sphere['Data'] = sphere.points[:, 2]
plotter = pv.Plotter()
_ = plotter.add_mesh(sphere, show_scalar_bar=False)
_ = plotter.add_scalar_bar('Data', interactive=True, vertical=False,
                           title_font_size=35,
                           label_font_size=30,
                           outline=True, fmt='%10.5f')
plotter.show()
