from pyvista import examples
mesh = examples.load_airplane()
mesh.actual_memory_size  # doctest:+SKIP
# Expected:
## 93
