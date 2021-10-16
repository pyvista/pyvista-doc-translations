# Create basic vector field.  This is a point cloud where each point
# has a vector and magnitude attached to it.
#
import pyvista
import numpy as np
x, y = np.meshgrid(np.linspace(-5,5,10),np.linspace(-5,5,10))
points = np.vstack((x.ravel(), y.ravel(), np.zeros(x.size))).T
u = x/np.sqrt(x**2 + y**2)
v = y/np.sqrt(x**2 + y**2)
vectors = np.vstack((u.ravel()**3, v.ravel()**3, np.zeros(u.size))).T
pdata = pyvista.vector_poly_data(points, vectors)
pdata.point_data.keys()
# Expected:
## ['vectors', 'mag']
#
# Convert these to arrows and plot it.
#
pdata.glyph(orient='vectors', scale='mag').plot()
