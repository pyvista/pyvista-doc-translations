# Create a ParametricRandomHills mesh.
#
import pyvista
mesh = pyvista.ParametricRandomHills()
mesh.plot(color='w', smooth_shading=True)
