# Create a "spring" using the rotational extrusion filter.
#
import pyvista
profile = pyvista.Polygon(center=[1.25, 0.0, 0.0], radius=0.2,
                          normal=(0, 1, 0), n_sides=30)
extruded = profile.extrude_rotate(resolution=360, translation=4.0,
                                  dradius=.5, angle=1500.0)
extruded.plot(smooth_shading=True)
#
# Create a "wine glass" using the rotational extrusion filter.
#
import numpy as np
points = np.array([[-0.18, 0, 0],
                   [-0.18, 0, 0.01],
                   [-0.18, 0, 0.02],
                   [-0.01, 0, 0.03],
                   [-0.01, 0, 0.04],
                   [-0.02, 0, 0.5],
                   [-0.05, 0, 0.75],
                   [-0.1, 0, 0.8],
                   [-0.2, 0, 1.0]])
spline = pyvista.Spline(points, 30)
extruded = spline.extrude_rotate(resolution=20)
extruded.plot(color='tan')
