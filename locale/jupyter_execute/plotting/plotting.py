#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyvista as pv
sphere = pv.Sphere()
sphere.plot(jupyter_backend='static')


# In[2]:


plotter = pv.Plotter(notebook=True)
plotter.add_mesh(sphere)
plotter.show(jupyter_backend='static')


# In[3]:


plotter = pv.Plotter(notebook=True)
plotter.add_mesh(sphere)
plotter.show(jupyter_backend='ipygany')

