# Create a partial sphere with a hole and then fill it.
#
import pyvista as pv
sphere_with_hole = pv.Sphere(end_theta=330)
sphere = sphere_with_hole.fill_holes(1000)  # doctest:+SKIP
edges = sphere.extract_feature_edges(feature_edges=False,
                                     manifold_edges=False)  # doctest:+SKIP
assert edges.n_cells == 0  # doctest:+SKIP
