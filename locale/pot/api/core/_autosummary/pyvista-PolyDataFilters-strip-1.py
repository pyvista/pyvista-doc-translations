from pyvista import examples
mesh = examples.load_airplane()
slc = mesh.slice(normal='z', origin=(0, 0, -10))
stripped = slc.strip()
stripped.n_cells
# Expected:
## 1
stripped.plot(show_edges=True, line_width=3)
