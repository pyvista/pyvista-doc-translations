import pyvista as pv
plotter = pv.Plotter(shape=(2, 2))
plotter.subplot(0, 0)
_ = plotter.add_mesh(pv.Box(), name='box')
plotter.subplot(0, 1)
_ = plotter.add_mesh(pv.Sphere(), name='sphere')
plotter.subplot(1, 0)
_ = plotter.add_mesh(pv.Box(), name='box')
plotter.subplot(1, 1)
_ = plotter.add_mesh(pv.Cone(), name='cone')
plotter.where_is('box')
# Expected:
## [(0, 0), (1, 0)]
#
plotter.show()
