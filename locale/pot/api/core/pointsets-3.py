# plot this displaced beam
plotter = pv.Plotter()
plotter.add_mesh(grid, scalars=d[:, 1],
                 scalar_bar_args={'title': 'Y Displacement'},
                 rng=[-d.max(), d.max()])
plotter.add_axes()
plotter.camera_position = cpos
plotter.show()