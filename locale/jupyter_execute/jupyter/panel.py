#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyvista import demos
demos.plot_logo(background='white', jupyter_backend='panel')


# In[2]:


import pyvista as pv
from pyvista import examples

# create a point cloud from lidar data and add height scalars
dataset = examples.download_lidar()
point_cloud = pv.PolyData(dataset.points[::100])
point_cloud['height'] = point_cloud.points[:, 2]
point_cloud.plot(window_size=[500, 500],
                 jupyter_backend='panel',
                 cmap='jet',
                 point_size=2,
                 background='w')


# In[3]:


import math
import numpy
import numpy as np

import pyvista
from pyvista import examples

# set the global jupyterlab backend.  All plots from this point
# onward will use the ``panel`` backend and do not have to be
# specified in ``show``
pyvista.set_jupyter_backend('panel')

# create a sphere for Mars
sphere = pyvista.Sphere(radius=1, theta_resolution=90, phi_resolution=90,
                        start_theta=270.001, end_theta=270)
sphere.t_coords = numpy.zeros((sphere.points.shape[0], 2))

sphere.t_coords[:, 0] = 0.5 + np.arctan2(-sphere.points[:, 0], sphere.points[:, 1])/(2 * math.pi)
sphere.t_coords[:, 1] = 0.5 + np.arcsin(sphere.points[:, 2]) / math.pi

tex = pyvista.read_texture(examples.download_mars_jpg())

# with a black background
pl = pyvista.Plotter(window_size=[500, 500])
pl.background_color = 'black'
pl.add_mesh(sphere, texture=tex, smooth_shading=False)
pl.show()

