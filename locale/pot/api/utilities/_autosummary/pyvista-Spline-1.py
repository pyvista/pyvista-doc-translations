# Construct a spline
#
import numpy as np
import pyvista as pv
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
points = np.column_stack((x, y, z))
spline = pv.Spline(points, 1000)
spline.plot(render_lines_as_tubes=True, line_width=10, show_scalar_bar=False)
