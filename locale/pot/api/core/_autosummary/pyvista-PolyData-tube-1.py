# Convert a single line to a tube.
#
import pyvista as pv
line = pv.Line()
tube = line.tube(radius=0.02)
f'Line Cells: {line.n_cells}'
# Expected:
## 'Line Cells: 1'
f'Tube Cells: {tube.n_cells}'
# Expected:
## 'Tube Cells: 22'
tube.plot(color='tan')
