# Return the active texture coordinates from the globe example.
#
from pyvista import examples
globe = examples.load_globe()
globe.active_t_coords
# Expected:
## pyvista_ndarray([[0.        , 0.        ],
##                  [0.        , 0.07142857],
##                  [0.        , 0.14285714],
##                  ...,
##                  [1.        , 0.85714286],
##                  [1.        , 0.92857143],
##                  [1.        , 1.        ]])
