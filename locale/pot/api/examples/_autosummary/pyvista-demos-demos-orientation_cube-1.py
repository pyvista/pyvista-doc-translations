# Load the cube mesh and plot it
#
import pyvista
from pyvista import demos
ocube = demos.orientation_cube()
pl = pyvista.Plotter()
_ = pl.add_mesh(ocube['cube'], show_edges=True)
_ = pl.add_mesh(ocube['x_p'], color='blue')
_ = pl.add_mesh(ocube['x_n'], color='blue')
_ = pl.add_mesh(ocube['y_p'], color='green')
_ = pl.add_mesh(ocube['y_n'], color='green')
_ = pl.add_mesh(ocube['z_p'], color='red')
_ = pl.add_mesh(ocube['z_n'], color='red')
pl.show_axes()
pl.show()
