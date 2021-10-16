# Intersect two spheres, returning the intersection and both spheres
# which have new points/cells along the intersection line.
#
import pyvista as pv
import numpy as np
s1 = pv.Sphere(phi_resolution=15, theta_resolution=15)
s2 = s1.copy()
s2.points += np.array([0.25, 0, 0])
intersection, s1_split, s2_split = s1.intersection(s2)
pl = pv.Plotter()
_ = pl.add_mesh(s1, style='wireframe')
_ = pl.add_mesh(s2, style='wireframe')
_ = pl.add_mesh(intersection, color='r', line_width=10)
pl.show()
#
# The mesh splitting takes additional time and can be turned
# off for either mesh individually.
#
intersection, _, s2_split = s1.intersection(s2,
                                            split_first=False,
                                            split_second=True)
