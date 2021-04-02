#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyvista import demos
demos.plot_logo(background='white', jupyter_backend='panel')


# In[2]:


from pyvista import demos

# basic glyphs demo
mesh = demos.glyphs(2)

text = demos.logo.text_3d("I'm interactive!", depth=0.2)
text.points *= 0.1
text.translate([0, 1.4, 1.5])
mesh += text
mesh['Example Scalars'] = mesh.points[:, 0]

mesh.plot(cpos='xy', jupyter_backend='ipygany', background='white',
          show_scalar_bar=True)

