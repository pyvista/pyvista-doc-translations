import pyvista
from pyvista import examples
grid = pyvista.read(examples.hexbeamfile)
subset = grid.extract_cells(range(20))
subset.n_cells
# Expected:
## 20
pl = pyvista.Plotter()
actor = pl.add_mesh(grid, style='wireframe', line_width=5, color='black')
actor = pl.add_mesh(subset, color='grey')
pl.show()
