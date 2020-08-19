.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_examples_03-advanced_antarctica-compare.py>`     to download the full example code
    .. rst-class:: sphx-glr-example-title

    .. _sphx_glr_examples_03-advanced_antarctica-compare.py:


Compare Field Across Mesh Regions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is some velocity data from a glacier modelling simulation that is compared
across nodes in the simulation. We have simplified the mesh to have the
simulation node value already on the mesh.

This was originally posted to `pyvista/pyvista-support#83 <https://github.com/pyvista/pyvista-support/issues/83>`_.

The modeling results are courtesy of `Urruty Benoit <https://github.com/BenoitURRUTY>`_
and  are from the `Elmer/Ice <http://elmerice.elmerfem.org>`_ simulation
software.



.. code-block:: default


    # sphinx_gallery_thumbnail_number = 2
    import pyvista as pv
    from pyvista import examples
    import numpy as np

    # Load the sample data
    mesh = examples.download_antarctica_velocity()
    mesh["magnitude"] = np.linalg.norm(mesh["ssavelocity"], axis=1)
    mesh






.. only:: builder_html

    .. raw:: html

        <table><tr><th>Header</th><th>Data Arrays</th></tr><tr><td>
        <table>
        <tr><th>PolyData</th><th>Information</th></tr>
        <tr><td>N Cells</td><td>1106948</td></tr>
        <tr><td>N Points</td><td>557470</td></tr>
        <tr><td>X Bounds</td><td>-2.506e+06, 2.743e+06</td></tr>
        <tr><td>Y Bounds</td><td>-2.143e+06, 2.240e+06</td></tr>
        <tr><td>Z Bounds</td><td>0.000e+00, 0.000e+00</td></tr>
        <tr><td>N Arrays</td><td>3</td></tr>
        </table>

        </td><td>
        <table>
        <tr><th>Name</th><th>Field</th><th>Type</th><th>N Comp</th><th>Min</th><th>Max</th></tr>
        <tr><td><b>ssavelocity</b></td><td>Points</td><td>float64</td><td>3</td><td>-4.341e+03</td><td>9.677e+03</td></tr>
        <tr><td>node_value</td><td>Points</td><td>int64</td><td>1</td><td>0.000e+00</td><td>2.300e+01</td></tr>
        <tr><td>magnitude</td><td>Points</td><td>float64</td><td>1</td><td>6.649e-03</td><td>1.013e+04</td></tr>
        </table>

        </td></tr> </table>
        <br />
        <br />

Here is a helper to extract regions of the mesh based on the simulation node.


.. code-block:: default


    def extract_node(node):
        idx = mesh["node_value"] == node
        return mesh.extract_points(idx)









.. code-block:: default


    p = pv.Plotter()
    p.add_mesh(mesh, scalars="node_value")
    for node in np.unique(mesh["node_value"]):
        loc = extract_node(node).center
        p.add_point_labels(loc, ["Node {}".format(node)])
    p.show(cpos="xy")






.. image:: /examples/03-advanced/images/sphx_glr_antarctica-compare_001.png
    :alt: antarctica compare
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(118637.09504000004, 48407.14021500014, 13210946.134298638),
     (118637.09504000004, 48407.14021500014, 0.0),
     (0.0, 1.0, 0.0)]




.. code-block:: default


    vel_dargs = dict(scalars="magnitude", clim=[1e-3, 1e4], cmap='Blues', log_scale=True)

    mesh.plot(cpos="xy", **vel_dargs)




.. image:: /examples/03-advanced/images/sphx_glr_antarctica-compare_002.png
    :alt: antarctica compare
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(118637.09504000004, 48407.14021500014, 13210946.134298638),
     (118637.09504000004, 48407.14021500014, 0.0),
     (0.0, 1.0, 0.0)]




.. code-block:: default


    a = extract_node(12)
    b = extract_node(20)









.. code-block:: default


    pl = pv.Plotter()
    pl.add_mesh(a, **vel_dargs)
    pl.add_mesh(b, **vel_dargs)
    pl.show(cpos='xy')




.. image:: /examples/03-advanced/images/sphx_glr_antarctica-compare_003.png
    :alt: antarctica compare
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(-1204058.8833615, 259736.8989715, 3426819.5414909166),
     (-1204058.8833615, 259736.8989715, 0.0),
     (0.0, 1.0, 0.0)]



plot vectors without mesh


.. code-block:: default


    pl = pv.Plotter()
    pl.add_mesh(a.glyph(orient="ssavelocity", factor=20), **vel_dargs)
    pl.add_mesh(b.glyph(orient="ssavelocity", factor=20), **vel_dargs)
    pl.camera_position = [(-1114684.6969340036, 293863.65389149904, 752186.603224546),
     (-1114684.6969340036, 293863.65389149904, 0.0),
     (0.0, 1.0, 0.0)]
    pl.show()





.. image:: /examples/03-advanced/images/sphx_glr_antarctica-compare_004.png
    :alt: antarctica compare
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(-1114684.6969340036, 293863.65389149904, 752186.603224546),
     (-1114684.6969340036, 293863.65389149904, 0.0),
     (0.0, 1.0, 0.0)]



Compare directions. Normalize them so we can get a reasonable direction
comparison.


.. code-block:: default


    flow_a = a.point_arrays['ssavelocity'].copy()
    flow_a /= np.linalg.norm(flow_a, axis=1).reshape(-1, 1)
    flow_b = b.point_arrays['ssavelocity'].copy()
    flow_b /= np.linalg.norm(flow_b, axis=1).reshape(-1, 1)


    # plot normalized vectors
    pl = pv.Plotter()
    pl.add_arrows(a.points, flow_a, mag=10000, color='b', label='flow_a')
    pl.add_arrows(b.points, flow_b, mag=10000, color='r', label='flow_b')
    pl.add_legend()
    pl.camera_position = [(-1044239.3240694795, 354805.0268606294, 484178.24825854995),
                          (-1044239.3240694795, 354805.0268606294, 0.0),
                          (0.0, 1.0, 0.0)]
    pl.show()





.. image:: /examples/03-advanced/images/sphx_glr_antarctica-compare_005.png
    :alt: antarctica compare
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(-1044239.3240694795, 354805.0268606294, 484178.24825854995),
     (-1044239.3240694795, 354805.0268606294, 0.0),
     (0.0, 1.0, 0.0)]



flow_a that agrees with the mean flow path of flow_b


.. code-block:: default

    agree = flow_a.dot(flow_b.mean(0))

    pl = pv.Plotter()
    pl.add_mesh(a, scalars=agree, cmap='bwr', stitle='Flow agreement with block b')
    pl.add_mesh(b, color='w')
    pl.show(cpos='xy')




.. image:: /examples/03-advanced/images/sphx_glr_antarctica-compare_006.png
    :alt: antarctica compare
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(-1204058.8833615, 259736.8989715, 3426819.5414909166),
     (-1204058.8833615, 259736.8989715, 0.0),
     (0.0, 1.0, 0.0)]




.. code-block:: default

    agree = flow_b.dot(flow_a.mean(0))

    pl = pv.Plotter()
    pl.add_mesh(a, color='w')
    pl.add_mesh(b, scalars=agree, cmap='bwr', stitle='Flow agreement with block a')
    pl.show(cpos='xy')



.. image:: /examples/03-advanced/images/sphx_glr_antarctica-compare_007.png
    :alt: antarctica compare
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(-1204058.8833615, 259736.8989715, 3426819.5414909166),
     (-1204058.8833615, 259736.8989715, 0.0),
     (0.0, 1.0, 0.0)]




.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  12.778 seconds)


.. _sphx_glr_download_examples_03-advanced_antarctica-compare.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download sphx-glr-download-python

     :download:`Download Python source code: antarctica-compare.py <antarctica-compare.py>`



  .. container:: sphx-glr-download sphx-glr-download-jupyter

     :download:`Download Jupyter notebook: antarctica-compare.ipynb <antarctica-compare.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
