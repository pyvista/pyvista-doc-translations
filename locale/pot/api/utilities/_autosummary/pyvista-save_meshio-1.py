# Save a pyvista sphere to a Abaqus data file.
#
import pyvista
sphere = pyvista.Sphere()
pyvista.save_meshio('mymesh.inp', sphere)  # doctest:+SKIP
