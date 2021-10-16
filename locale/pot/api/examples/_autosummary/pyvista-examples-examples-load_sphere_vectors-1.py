from pyvista import examples
mesh = examples.load_sphere_vectors()
mesh.point_data
# Expected:
## pyvista DataSetAttributes
## Association     : POINT
## Active Scalars  : vectors
## Active Vectors  : vectors
## Active Texture  : None
## Active Normals  : Normals
## Contains arrays :
##     Normals                 float32  (842, 3)             NORMALS
##     vectors                 float32  (842, 3)             VECTORS
