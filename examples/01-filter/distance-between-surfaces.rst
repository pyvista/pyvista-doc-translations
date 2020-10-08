.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_examples_01-filter_distance-between-surfaces.py>`     to download the full example code
    .. rst-class:: sphx-glr-example-title

    .. _sphx_glr_examples_01-filter_distance-between-surfaces.py:


Distance Between Two Surfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compute the average thickness between two surfaces.

For example, you might have two surfaces that represent the boundaries of
lithological layers in a subsurface geological model and you want to know the
average thickness of a unit between those boundaries.

We can compute the thickness between the two surfaces using a few different
methods. First, we will demo a method where we compute the normals of the
bottom surface, and then project a ray to the top surface to compute the
distance along the surface normals. Second, we will use a KDTree to compute
the distance from eevery point in the bottom mesh to it's closest point in
the top mesh.


.. code-block:: default

    import pyvista as pv
    import numpy as np

    # A helper to make a random surface
    def hill(seed):
        mesh = pv.ParametricRandomHills(randomseed=seed,
                                        hillamplitude=0.5)
        mesh.rotate_y(80) # give the surfaces some tilt
        return mesh

    h0 = hill(1).elevation()
    h1 = hill(10)
    # Shift one surface
    h1.points[:,-1] += 5
    h1 = h1.elevation()









.. code-block:: default


    p = pv.Plotter()
    p.add_mesh(h0)
    p.add_mesh(h1)
    p.show_grid()
    p.show()




.. image:: /examples/01-filter/images/sphx_glr_distance-between-surfaces_001.png
    :alt: distance between surfaces
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(32.9280789042912, 43.08363415255168, 35.88714410318951),
     (-0.15555524826049805, 9.99999999999999, 2.8035099506378174),
     (0.0, 0.0, 1.0)]



Ray Tracing Distance
++++++++++++++++++++

Compute normals of lower surface


.. code-block:: default

    h0n = h0.compute_normals(point_normals=True, cell_normals=False,
                             auto_orient_normals=True, )








Travel along noramals to the other surface and compute the thickness on each
vector.


.. code-block:: default


    h0n["distances"] = np.empty(h0.n_points)
    for i in range(h0n.n_points):
        p = h0n.points[i]
        vec = h0n["Normals"][i] * h0n.length
        p0 = p - vec
        p1 = p + vec
        ip, ic = h1.ray_trace(p0, p1, first_point=True)
        dist = np.sqrt(np.sum((ip - p)**2))
        h0n["distances"][i] = dist

    # Replace zeros with nans
    mask = h0n["distances"] == 0
    h0n["distances"][mask] = np.nan
    np.nanmean(h0n["distances"])





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    5.14863403912341




.. code-block:: default

    p = pv.Plotter()
    p.add_mesh(h0n, scalars="distances")
    p.add_mesh(h1, color=True, opacity=0.75)
    p.show()





.. image:: /examples/01-filter/images/sphx_glr_distance-between-surfaces_002.png
    :alt: distance between surfaces
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(32.9280789042912, 43.08363415255168, 35.88714410318951),
     (-0.15555524826049805, 9.99999999999999, 2.8035099506378174),
     (0.0, 0.0, 1.0)]



Nearest Neighbor Distance
+++++++++++++++++++++++++

You could also use a KDTree to compare the distance between each point of the
upper surface and the nearest neighbor of the lower surface.
This won't be the exact surface to surface distance, but it will be
noticeably faster than a ray trace, especially for large surfaces.


.. code-block:: default

    from scipy.spatial import KDTree

    tree = KDTree(h1.points)
    d, idx = tree.query(h0.points )
    h0["distances"] = d
    np.mean(d)





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    4.842395354562363




.. code-block:: default

    p = pv.Plotter()
    p.add_mesh(h0, scalars="distances")
    p.add_mesh(h1, color=True, opacity=0.75)
    p.show()



.. image:: /examples/01-filter/images/sphx_glr_distance-between-surfaces_003.png
    :alt: distance between surfaces
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(32.9280789042912, 43.08363415255168, 35.88714410318951),
     (-0.15555524826049805, 9.99999999999999, 2.8035099506378174),
     (0.0, 0.0, 1.0)]




.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  30.164 seconds)


.. _sphx_glr_download_examples_01-filter_distance-between-surfaces.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download sphx-glr-download-python

     :download:`Download Python source code: distance-between-surfaces.py <distance-between-surfaces.py>`



  .. container:: sphx-glr-download sphx-glr-download-jupyter

     :download:`Download Jupyter notebook: distance-between-surfaces.ipynb <distance-between-surfaces.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
