from pyvista import examples
grid = examples.load_hydrogen_orbital(3, 2, -2)
grid.plot(volume=True, opacity=[1, 0, 1], cmap='magma')