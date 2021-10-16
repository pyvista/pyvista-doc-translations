from pyvista import examples
mesh = examples.load_airplane()
mesh.cell_points(0)  # doctest:+SKIP
# Expected:
## [[896.99401855  48.76010132  82.26560211]
##  [906.59301758  48.76010132  80.74520111]
##  [907.53900146  55.49020004  83.65809631]]
