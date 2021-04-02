#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyvista as pv
pv.set_jupyter_backend('panel')
pv.set_plot_theme('document')


# In[2]:


import numpy as np
import pyvista as pv

nodes = np.random.rand(100, 3)
mesh = pv.PolyData(nodes)
mesh.plot(point_size=10)


# In[3]:


from pyvista import examples

mesh = examples.load_hexbeam()
bcpos = [(6.20, 3.00, 7.50),
         (0.16, 0.13, 2.65),
         (-0.28, 0.94, -0.21)]

pl = pv.Plotter()
pl.add_mesh(mesh, show_edges=True, color='white')
pl.add_mesh(pv.PolyData(mesh.points), color='red',
       point_size=10, render_points_as_spheres=True)
pl.camera_position = bcpos
pl.show()


# In[4]:


mesh = examples.download_bunny_coarse()

pl = pv.Plotter()
pl.add_mesh(mesh, show_edges=True, color='white')
pl.add_mesh(pv.PolyData(mesh.points), color='red',
            point_size=10, render_points_as_spheres=True)
pl.camera_position = [(0.02, 0.30, 0.73),
                      (0.02, 0.03, -0.022),
                      (-0.03, 0.94, -0.34)]
pl.show()


# In[5]:


mesh = examples.load_hexbeam()

pl = pv.Plotter()
pl.add_mesh(mesh, show_edges=True, color='white')
pl.add_mesh(pv.PolyData(mesh.points), color='red',
            point_size=10, render_points_as_spheres=True)

pl.add_mesh(mesh.extract_cells(mesh.n_cells-1),
            color='pink', edge_color='blue',
            line_width=5, show_edges=True)

pl.camera_position = [(6.20, 3.00, 7.50),
                      (0.16, 0.13, 2.65),
                      (-0.28, 0.94, -0.21)]
pl.show()


# In[6]:


mesh.point_arrays['my point values'] = np.arange(mesh.n_points)

mesh.plot(scalars='my point values', cpos=bcpos,
          show_edges=True)


# In[7]:


mesh.cell_arrays['my cell values'] = np.arange(mesh.n_cells)
mesh.plot(scalars='my cell values', cpos=bcpos,
          show_edges=True)


# In[8]:


mesh = examples.load_uniform()

pl = pv.Plotter(shape=(1,2))
pl.add_mesh(mesh, scalars='Spatial Point Data', show_edges=True)
pl.subplot(0,1)
pl.add_mesh(mesh, scalars='Spatial Cell Data', show_edges=True)
pl.show()

