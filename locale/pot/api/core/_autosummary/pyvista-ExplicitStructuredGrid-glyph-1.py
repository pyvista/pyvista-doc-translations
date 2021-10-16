# Create arrow glyphs oriented by vectors and scaled by scalars.
# Factor parameter is used to reduce the size of the arrows.
#
import pyvista
from pyvista import examples
mesh = examples.load_random_hills()
arrows = mesh.glyph(scale="Normals", orient="Normals", tolerance=0.05)
pl = pyvista.Plotter()
actor = pl.add_mesh(arrows, color="black")
actor = pl.add_mesh(mesh, scalars="Elevation", cmap="terrain",
                    show_scalar_bar=False)
pl.show()
#
# See :ref:`glyph_example` and :ref:`glyph_table_example` for more
