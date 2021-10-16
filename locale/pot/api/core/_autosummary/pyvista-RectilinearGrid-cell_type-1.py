from pyvista import examples
mesh = examples.load_airplane()
mesh.cell_type(0)
# Expected:
## 5
