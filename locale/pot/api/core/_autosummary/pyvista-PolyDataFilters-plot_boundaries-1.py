from pyvista import examples
hills = examples.load_random_hills()
hills.plot_boundaries(line_width=10)
