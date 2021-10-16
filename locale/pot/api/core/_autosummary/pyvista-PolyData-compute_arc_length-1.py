import pyvista as pv
sphere = pv.Sphere()
path = sphere.geodesic(0, 100)
length = path.compute_arc_length()['arc_length'][-1]
f'Length is {length:.3f}'
# Expected:
## 'Length is 0.812'
#
# This is identical to the geodesic_distance.
#
length = sphere.geodesic_distance(0, 100)
f'Length is {length:.3f}'
# Expected:
## 'Length is 0.812'
#
# You can also plot the arc_length.
#
arc = path.compute_arc_length()
arc.plot(scalars="arc_length")
