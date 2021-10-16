import pyvista
sphere = pyvista.Sphere()
sphere['Data'] = sphere.points[:, 2]
plotter = pyvista.Plotter()
_ = plotter.add_mesh(sphere)
plotter.scalar_bars
# Expected:
## Scalar Bar Title     Interactive
## "Data"               False
#
# Select a scalar bar actor based on the title of the bar.
#
plotter.scalar_bars['Data']  # doctest:+SKIP
# Expected:
## (vtkmodules.vtkRenderingAnnotation.vtkScalarBarActor)0x7fcd3567ca00
