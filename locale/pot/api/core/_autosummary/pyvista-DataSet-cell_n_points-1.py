from pyvista import examples
mesh = examples.load_airplane()
mesh.cell_n_points(0)
# Expected:
## 3
