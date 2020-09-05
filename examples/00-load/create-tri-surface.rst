.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_examples_00-load_create-tri-surface.py>`     to download the full example code
    .. rst-class:: sphx-glr-example-title

    .. _sphx_glr_examples_00-load_create-tri-surface.py:


Create Triangulated Surface
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a surface from a set of points through a Delaunay triangulation.


.. code-block:: default


    # sphinx_gallery_thumbnail_number = 2
    import pyvista as pv
    import numpy as np








Simple Traingulations
+++++++++++++++++++++

First, create some points for the surface.


.. code-block:: default


    # Define a simple Gaussian surface
    n = 20
    x = np.linspace(-200, 200, num=n) + np.random.uniform(-5, 5, size=n)
    y = np.linspace(-200, 200, num=n) + np.random.uniform(-5, 5, size=n)
    xx, yy = np.meshgrid(x, y)
    A, b = 100, 100
    zz = A * np.exp(-0.5 * ((xx / b) ** 2.0 + (yy / b) ** 2.0))

    # Get the points as a 2D NumPy array (N by 3)
    points = np.c_[xx.reshape(-1), yy.reshape(-1), zz.reshape(-1)]
    points[0:5, :]





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    array([[-199.07819595, -204.27776621,    1.71102652],
           [-176.17176538, -204.27776621,    2.62971468],
           [-162.29925906, -204.27776621,    3.32559107],
           [-137.17371107, -204.27776621,    4.84461872],
           [-117.23098818, -204.27776621,    6.24352339]])



Now use those points to create a point cloud PyVista data object. This will
be encompassed in a :class:`pyvista.PolyData` object.


.. code-block:: default


    # simply pass the numpy points to the PolyData constructor
    cloud = pv.PolyData(points)
    cloud.plot(point_size=15)




.. image:: /examples/00-load/images/sphx_glr_create-tri-surface_001.png
    :alt: create tri surface
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(642.6410622648111, 636.7625771584313, 691.2886776710488),
     (1.5521794492321703, -4.326305657147643, 50.199794855469946),
     (0.0, 0.0, 1.0)]



Now that we have a PyVista data structure of the points, we can perform a
triangulation to turn those boring discrete points into a connected surface.


.. code-block:: default


    surf = cloud.delaunay_2d()
    surf.plot(show_edges=True)





.. image:: /examples/00-load/images/sphx_glr_create-tri-surface_002.png
    :alt: create tri surface
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(642.6410622648111, 636.7625771584313, 691.2886776710488),
     (1.5521794492321703, -4.326305657147643, 50.199794855469946),
     (0.0, 0.0, 1.0)]



Masked Triangulations
+++++++++++++++++++++



.. code-block:: default


    x = np.arange(10, dtype=float)
    xx, yy, zz = np.meshgrid(x, x, [0])
    points = np.column_stack((xx.ravel(order="F"),
                              yy.ravel(order="F"),
                              zz.ravel(order="F")))
    # Perturb the points
    points[:, 0] += np.random.rand(len(points)) * 0.3
    points[:, 1] += np.random.rand(len(points)) * 0.3
    # Create the point cloud mesh to triangulate from the coordinates
    cloud = pv.PolyData(points)
    cloud






.. raw:: html


    <table>
    <tr><th>PolyData</th><th>Information</th></tr>
    <tr><td>N Cells</td><td>100</td></tr>
    <tr><td>N Points</td><td>100</td></tr>
    <tr><td>X Bounds</td><td>3.348e-03, 9.288e+00</td></tr>
    <tr><td>Y Bounds</td><td>2.205e-02, 9.251e+00</td></tr>
    <tr><td>Z Bounds</td><td>0.000e+00, 0.000e+00</td></tr>
    <tr><td>N Arrays</td><td>0</td></tr>
    </table>


    <br />
    <br />

Run the triangulation on these points


.. code-block:: default

    surf = cloud.delaunay_2d()
    surf.plot(cpos="xy", show_edges=True)





.. image:: /examples/00-load/images/sphx_glr_create-tri-surface_003.png
    :alt: create tri surface
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(4.645674369423264, 4.636357903595629, 25.28971591327551),
     (4.645674369423264, 4.636357903595629, 0.0),
     (0.0, 1.0, 0.0)]



Note that some of the outer edges are unconstrained and the triangulation
added unwanted triangles. We cn mitigate that with the ``alpha`` parameter.


.. code-block:: default

    surf = cloud.delaunay_2d(alpha=1.0)
    surf.plot(cpos="xy", show_edges=True)





.. image:: /examples/00-load/images/sphx_glr_create-tri-surface_004.png
    :alt: create tri surface
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(4.645674369423264, 4.636357903595629, 25.28971591327551),
     (4.645674369423264, 4.636357903595629, 0.0),
     (0.0, 1.0, 0.0)]



We could also add a polygon to ignore during the triangulation via the
``edge_source`` parameter.


.. code-block:: default


    # Define a polygonal hole with a clockwise polygon
    ids = [22, 23, 24, 25, 35, 45, 44, 43, 42, 32]

    # Create a polydata to store the boundary
    polygon = pv.PolyData()
    # Make sure it has the same points as the mesh being triangulated
    polygon.points = points
    # But only has faces in regions to ignore
    polygon.faces = np.array([len(ids),] + ids)

    surf = cloud.delaunay_2d(alpha=1.0, edge_source=polygon)

    p = pv.Plotter()
    p.add_mesh(surf, show_edges=True)
    p.add_mesh(polygon, color="red", opacity=0.5)
    p.show(cpos="xy")



.. image:: /examples/00-load/images/sphx_glr_create-tri-surface_005.png
    :alt: create tri surface
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(4.645674369423264, 4.636357903595629, 25.28971591327551),
     (4.645674369423264, 4.636357903595629, 0.0),
     (0.0, 1.0, 0.0)]




.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  3.634 seconds)


.. _sphx_glr_download_examples_00-load_create-tri-surface.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download sphx-glr-download-python

     :download:`Download Python source code: create-tri-surface.py <create-tri-surface.py>`



  .. container:: sphx-glr-download sphx-glr-download-jupyter

     :download:`Download Jupyter notebook: create-tri-surface.ipynb <create-tri-surface.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
