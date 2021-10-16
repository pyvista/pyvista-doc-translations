import pyvista
import numpy as np
cylinder = pyvista.Cylinder(center=[1, 2, 3], direction=[1, 1, 1],
                            radius=1, height=2)
cylinder.plot(show_edges=True, line_width=5, cpos='xy')
