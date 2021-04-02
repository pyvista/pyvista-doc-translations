#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyvista as pv
from pyvista import examples

mesh = examples.download_bunny()

pl = pv.Plotter()
pl.add_mesh(mesh, color='lightgrey')
pl.background_color = 'white'
pl.camera_position = 'xy'
pl.show(jupyter_backend='ipygany')


# In[2]:


import pyvista as pv
from pyvista import examples

pv.set_jupyter_backend('ipygany')

# download an example and reduce the mesh density
mesh = examples.download_carburator()
mesh.decimate(0.5, inplace=True)

# plot it on a white background with a lightgrey mesh color
mesh.plot(background='w', color='lightgrey')


# In[3]:


from ipywidgets import TwoByTwoLayout

import pyvista as pv


# consistent view options for all plotters
plot_kwargs = {'color': 'tan', 'jupyter_backend': 'ipygany',
               'return_viewer': True, 'background': 'white'}

supertoroid = pv.ParametricSuperToroid(n1=0.5)
scene_0 = supertoroid.plot(**plot_kwargs)

ellipsoid = pv.ParametricEllipsoid(10, 5, 5)
scene_1 = ellipsoid.plot(**plot_kwargs)

pseudosphere = pv.ParametricPseudosphere()
scene_2 = pseudosphere.plot(**plot_kwargs)

conicspiral = pv.ParametricConicSpiral()
scene_3 = conicspiral.plot(**plot_kwargs)

TwoByTwoLayout(top_left=scene_0,
               top_right=scene_1,
               bottom_left=scene_2,
               bottom_right=scene_3)


# In[4]:


# Load St Helens DEM and warp the topography
mesh = examples.download_st_helens().warp_by_scalar()

pl = pv.Plotter()
pl.background_color = 'white'
pl.add_mesh(mesh)
pl.show()

