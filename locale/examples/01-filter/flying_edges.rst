
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "examples/01-filter/flying_edges.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        :ref:`Go to the end <sphx_glr_download_examples_01-filter_flying_edges.py>`
        to download the full example code

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_examples_01-filter_flying_edges.py:


.. _marching_cubes_example:

Marching Cubes
~~~~~~~~~~~~~~

Generate a surface from a scalar field using the flying edges and
marching cubes filters as provided by the :func:`contour
<pyvista.DataSetFilters.contour>` filter.

Special thanks to GitHub user `stla <https://gist.github.com/stla>`_
for providing examples.

.. GENERATED FROM PYTHON SOURCE LINES 15-19

.. code-block:: default

    import numpy as np

    import pyvista as pv








.. GENERATED FROM PYTHON SOURCE LINES 20-24

Spider Cage
~~~~~~~~~~~
Use the marching cubes algorithm to extract the isosurface
generated from the spider cage function.

.. GENERATED FROM PYTHON SOURCE LINES 24-54

.. code-block:: default


    a = 0.9


    def spider_cage(x, y, z):
        x2 = x * x
        y2 = y * y
        x2_y2 = x2 + y2
        return (np.sqrt((x2 - y2) ** 2 / x2_y2 + 3 * (z * np.sin(a)) ** 2) - 3) ** 2 + 6 * (
            np.sqrt((x * y) ** 2 / x2_y2 + (z * np.cos(a)) ** 2) - 1.5
        ) ** 2


    # create a uniform grid to sample the function with
    n = 100
    x_min, y_min, z_min = -5, -5, -3
    grid = pv.ImageData(
        dimensions=(n, n, n),
        spacing=(abs(x_min) / n * 2, abs(y_min) / n * 2, abs(z_min) / n * 2),
        origin=(x_min, y_min, z_min),
    )
    x, y, z = grid.points.T

    # sample and plot
    values = spider_cage(x, y, z)
    mesh = grid.contour([1], values, method='marching_cubes')
    dist = np.linalg.norm(mesh.points, axis=1)
    mesh.plot(scalars=dist, smooth_shading=True, cmap="plasma", show_scalar_bar=False)









.. tab-set::



   .. tab-item:: Static Scene



            
     .. image-sg:: /examples/01-filter/images/sphx_glr_flying_edges_001.png
        :alt: flying edges
        :srcset: /examples/01-filter/images/sphx_glr_flying_edges_001.png
        :class: sphx-glr-single-img
     


   .. tab-item:: Interactive Scene



       .. offlineviewer:: /home/runner/work/pyvista-doc-translations/pyvista-doc-translations/pyvista/doc/source/examples/01-filter/images/sphx_glr_flying_edges_001.vtksz






.. GENERATED FROM PYTHON SOURCE LINES 55-59

Barth Sextic
~~~~~~~~~~~~
Use the flying edges algorithm to extract the isosurface
generated from the Barth sextic function.

.. GENERATED FROM PYTHON SOURCE LINES 59-96

.. code-block:: default



    phi = (1 + np.sqrt(5)) / 2
    phi2 = phi * phi


    def barth_sextic(x, y, z):
        x2 = x * x
        y2 = y * y
        z2 = z * z
        arr = (
            3 * (phi2 * x2 - y2) * (phi2 * y2 - z2) * (phi2 * z2 - x2)
            - (1 + 2 * phi) * (x2 + y2 + z2 - 1) ** 2
        )
        nan_mask = x2 + y2 + z2 > 3.1
        arr[nan_mask] = np.nan
        return arr


    # create a uniform grid to sample the function with
    n = 100
    k = 2.0
    x_min, y_min, z_min = -k, -k, -k
    grid = pv.ImageData(
        dimensions=(n, n, n),
        spacing=(abs(x_min) / n * 2, abs(y_min) / n * 2, abs(z_min) / n * 2),
        origin=(x_min, y_min, z_min),
    )
    x, y, z = grid.points.T

    # sample and plot
    values = barth_sextic(x, y, z)
    mesh = grid.contour([0], values, method='flying_edges')
    dist = np.linalg.norm(mesh.points, axis=1)
    mesh.plot(scalars=dist, smooth_shading=True, cmap="plasma", show_scalar_bar=False)









.. tab-set::



   .. tab-item:: Static Scene



            
     .. image-sg:: /examples/01-filter/images/sphx_glr_flying_edges_002.png
        :alt: flying edges
        :srcset: /examples/01-filter/images/sphx_glr_flying_edges_002.png
        :class: sphx-glr-single-img
     


   .. tab-item:: Interactive Scene



       .. offlineviewer:: /home/runner/work/pyvista-doc-translations/pyvista-doc-translations/pyvista/doc/source/examples/01-filter/images/sphx_glr_flying_edges_002.vtksz






.. GENERATED FROM PYTHON SOURCE LINES 97-101

Animate Barth Sextic
~~~~~~~~~~~~~~~~~~~~
Show 20 frames of various isocurves extracted from the Barth sextic
function.

.. GENERATED FROM PYTHON SOURCE LINES 101-128

.. code-block:: default



    def angle_to_range(angle):
        return -2 * np.sin(angle)


    pl = pv.Plotter(window_size=[800, 800], off_screen=True)

    pl.open_gif('barth_sextic.gif')

    for angle in np.linspace(0, np.pi, 20, endpoint=False):
        # clear the plotter before adding each frame's mesh
        pl.clear()
        pl.enable_lightkit()
        mesh = grid.contour([angle_to_range(angle)], values, method='flying_edges')
        dist = np.linalg.norm(mesh.points, axis=1)
        pl.add_mesh(
            mesh,
            scalars=dist,
            smooth_shading=True,
            rng=[0.5, 1.5],
            cmap="plasma",
            show_scalar_bar=False,
        )
        pl.write_frame()

    pl.close()




.. image-sg:: /examples/01-filter/images/sphx_glr_flying_edges_003.gif
   :alt: flying edges
   :srcset: /examples/01-filter/images/sphx_glr_flying_edges_003.gif
   :class: sphx-glr-single-img








.. rst-class:: sphx-glr-timing

   **Total running time of the script:** (0 minutes 6.779 seconds)


.. _sphx_glr_download_examples_01-filter_flying_edges.py:

.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-example




    .. container:: sphx-glr-download sphx-glr-download-python

      :download:`Download Python source code: flying_edges.py <flying_edges.py>`

    .. container:: sphx-glr-download sphx-glr-download-jupyter

      :download:`Download Jupyter notebook: flying_edges.ipynb <flying_edges.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
