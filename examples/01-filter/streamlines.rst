.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_examples_01-filter_streamlines.py>`     to download the full example code
    .. rst-class:: sphx-glr-example-title

    .. _sphx_glr_examples_01-filter_streamlines.py:


Streamlines
~~~~~~~~~~~

Integrate a vector field to generate streamlines.

This example generates streamlines of blood velocity. An isosurface of speed
provides context. The starting positions for the streamtubes were determined
by experimenting with the data.


.. code-block:: default


    # sphinx_gallery_thumbnail_number = 3
    import numpy as np
    import pyvista as pv
    from pyvista import examples








Carotid
+++++++
Download a sample dataset containing a vector field that can be integrated.


.. code-block:: default


    mesh = examples.download_carotid()








Run the stream line filtering algorithm.


.. code-block:: default


    streamlines, src = mesh.streamlines(
        return_source=True,
        max_time=100.0,
        initial_step_length=2.0,
        terminal_speed=0.1,
        n_points=25,
        source_radius=2.0,
        source_center=(133.1, 116.3, 5.0),
    )








Display the results! Please note that because this dataset's velocity field
was measured with low resolution, many streamlines travel outside the artery.


.. code-block:: default


    p = pv.Plotter()
    p.add_mesh(mesh.outline(), color="k")
    p.add_mesh(streamlines.tube(radius=0.15))
    p.add_mesh(src)
    p.add_mesh(mesh.contour([160]).extract_all_edges(), color="grey", opacity=0.25)
    p.camera_position = [(182.0, 177.0, 50), (139, 105, 19), (-0.2, -0.2, 1)]
    p.show()





.. image:: /examples/01-filter/images/sphx_glr_streamlines_001.png
    :alt: streamlines
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(182.0, 177.0, 50.0),
     (139.0, 105.0, 19.0),
     (-0.19245008972987523, -0.19245008972987523, 0.9622504486493761)]



Blood Vessels
+++++++++++++
Here is another example of blood flow:


.. code-block:: default


    mesh = examples.download_blood_vessels().cell_data_to_point_data()
    mesh.set_active_scalars("velocity")
    streamlines, src = mesh.streamlines(
        return_source=True, source_radius=10, source_center=(92.46, 74.37, 135.5)
    )










.. code-block:: default

    boundary = mesh.decimate_boundary().extract_all_edges()

    p = pv.Plotter()
    p.add_mesh(streamlines.tube(radius=0.2), lighting=False)
    p.add_mesh(src)
    p.add_mesh(boundary, color="grey", opacity=0.25)
    p.camera_position = [(10, 9.5, -43), (87.0, 73.5, 123.0), (-0.5, -0.7, 0.5)]
    p.show()





.. image:: /examples/01-filter/images/sphx_glr_streamlines_002.png
    :alt: streamlines
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(10.0, 9.5, -43.0),
     (87.0, 73.5, 123.0),
     (-0.502518907629606, -0.7035264706814484, 0.502518907629606)]



Kitchen
+++++++



.. code-block:: default

    kpos = [(-6.68, 11.9, 11.6), (3.5, 2.5, 1.26), (0.45, -0.4, 0.8)]

    mesh = examples.download_kitchen()
    kitchen = examples.download_kitchen(split=True)









.. code-block:: default

    streamlines = mesh.streamlines(n_points=40, source_center=(0.08, 3, 0.71))









.. code-block:: default

    p = pv.Plotter()
    p.add_mesh(mesh.outline(), color="k")
    p.add_mesh(kitchen, color=True)
    p.add_mesh(streamlines.tube(radius=0.01), scalars="velocity", lighting=False)
    p.camera_position = kpos
    p.show()





.. image:: /examples/01-filter/images/sphx_glr_streamlines_003.png
    :alt: streamlines
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(-6.68, 11.9, 11.6),
     (3.5, 2.5, 1.26),
     (0.4494385524950301, -0.39950093555113786, 0.7990018711022757)]



Custom 3D Vector Field
++++++++++++++++++++++



.. code-block:: default


    nx = 20
    ny = 15
    nz = 5

    origin = (-(nx - 1)*0.1/2, -(ny - 1)*0.1/2, -(nz - 1)*0.1/2)
    mesh = pv.UniformGrid((nx, ny, nz), (.1, .1, .1), origin)
    x = mesh.points[:, 0]
    y = mesh.points[:, 1]
    z = mesh.points[:, 2]
    vectors = np.empty((mesh.n_points, 3))
    vectors[:, 0] = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
    vectors[:, 1] = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
    vectors[:, 2] = (np.sqrt(3.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
                     np.sin(np.pi * z))

    mesh['vectors'] = vectors








.. code-block:: default

    stream, src = mesh.streamlines('vectors', return_source=True,
                                   terminal_speed=0.0, n_points=200,
                                   source_radius=0.1)








.. code-block:: default

    cpos = [(1.2, 1.2, 1.2), (-0.0, -0.0, -0.0), (0.0, 0.0, 1.0)]
    stream.tube(radius=0.0015).plot(cpos=cpos)



.. image:: /examples/01-filter/images/sphx_glr_streamlines_004.png
    :alt: streamlines
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(1.2, 1.2, 1.2),
     (0.0, 0.0, 0.0),
     (0.0, 0.0, 1.0)]




.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  15.699 seconds)


.. _sphx_glr_download_examples_01-filter_streamlines.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download sphx-glr-download-python

     :download:`Download Python source code: streamlines.py <streamlines.py>`



  .. container:: sphx-glr-download sphx-glr-download-jupyter

     :download:`Download Jupyter notebook: streamlines.ipynb <streamlines.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
