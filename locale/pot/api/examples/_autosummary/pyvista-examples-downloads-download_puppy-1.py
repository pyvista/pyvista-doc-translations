from pyvista import examples
dataset = examples.download_puppy()  # doctest:+SKIP
dataset  # doctest:+SKIP
# Expected:
## UniformGrid (0x7fa0c15079a0)
## N Cells:    1917201
## N Points:   1920000
## X Bounds:   0.000e+00, 1.599e+03
## Y Bounds:   0.000e+00, 1.199e+03
## Z Bounds:   0.000e+00, 0.000e+00
## Dimensions: 1600, 1200, 1
## Spacing:    1.000e+00, 1.000e+00, 1.000e+00
## N Arrays:   1
