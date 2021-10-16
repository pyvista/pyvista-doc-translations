# Convert a line to a ribbon and plot it.
#
import numpy as np
import pyvista
n = 1000
theta = np.linspace(-10 * np.pi, 10 * np.pi, n)
z = np.linspace(-2, 2, n)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
points = np.column_stack((x, y, z))
pdata = pyvista.PolyData(points)
pdata.lines = np.hstack((n, range(n)))
pdata['distance'] = range(n)
ribbon = pdata.ribbon(width=0.2)
ribbon.plot(show_scalar_bar=False)
