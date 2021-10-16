# Generate the "elevation" scalars for a sphere mesh.  This is
# simply the height in Z from the XY plane.
#
import pyvista
sphere = pyvista.Sphere()
sphere_elv = sphere.elevation()
sphere_elv.plot(smooth_shading=True)
#
# Access the first 4 elevation scalars.  This is a point-wise
# array containing the "elevation" of each point.
#
sphere_elv['Elevation'][:4]  # doctest:+SKIP
# Expected:
## array([-0.5       ,  0.5       , -0.49706897, -0.48831028], dtype=float32)
