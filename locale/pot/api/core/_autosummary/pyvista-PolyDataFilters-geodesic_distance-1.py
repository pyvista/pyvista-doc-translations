import pyvista as pv
sphere = pv.Sphere()
length = sphere.geodesic_distance(0, 100)
f'Length is {length:.3f}'
# Expected:
## 'Length is 0.812'
