.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_examples_01-filter_voxelize.py>`     to download the full example code
    .. rst-class:: sphx-glr-example-title

    .. _sphx_glr_examples_01-filter_voxelize.py:


Voxelize a Surface Mesh
~~~~~~~~~~~~~~~~~~~~~~~

Create a voxel model (like legos) of a closed surface or volumetric mesh.

This example also demonstrates how to compute an implicit distance from a
bounding :class:`pyvista.PolyData` surface.



.. code-block:: default

    # sphinx_gallery_thumbnail_number = 2
    from pyvista import examples
    import pyvista as pv
    import numpy as np

    # Load a surface to voxelize
    surface = examples.download_foot_bones()
    surface






.. only:: builder_html

    .. raw:: html


        <table>
        <tr><th>PolyData</th><th>Information</th></tr>
        <tr><td>N Cells</td><td>4204</td></tr>
        <tr><td>N Points</td><td>2154</td></tr>
        <tr><td>X Bounds</td><td>-5.633e+00, 5.633e+00</td></tr>
        <tr><td>Y Bounds</td><td>-1.860e+00, 1.860e+00</td></tr>
        <tr><td>Z Bounds</td><td>-2.125e+00, 2.126e+00</td></tr>
        <tr><td>N Arrays</td><td>0</td></tr>
        </table>


        <br />
        <br />


.. code-block:: default

    cpos = [(7.656346967151718, -9.802071079151158, -11.021236183314311),
     (0.2224512272564101, -0.4594554282112895, 0.5549738359311297),
     (-0.6279216753504941, -0.7513057097368635, 0.20311105371647392)]

    surface.plot(cpos=cpos, opacity=0.75)





.. image:: /examples/01-filter/images/sphx_glr_voxelize_001.png
    :alt: voxelize
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(7.656346967151718, -9.802071079151158, -11.021236183314311),
     (0.2224512272564101, -0.4594554282112895, 0.5549738359311297),
     (-0.6279216753504943, -0.7513057097368636, 0.20311105371647395)]



Create a voxel model of the bounding surface


.. code-block:: default

    voxels = pv.voxelize(surface, density=surface.length/200)

    p = pv.Plotter()
    p.add_mesh(voxels, color=True, show_edges=True, opacity=0.5)
    p.add_mesh(surface, color="lightblue", opacity=0.5)
    p.show(cpos=cpos)





.. image:: /examples/01-filter/images/sphx_glr_voxelize_002.png
    :alt: voxelize
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(7.656346967151718, -9.802071079151158, -11.021236183314311),
     (0.2224512272564101, -0.4594554282112895, 0.5549738359311297),
     (-0.6279216753504943, -0.7513057097368636, 0.20311105371647395)]



We could even add a scalar field to that new voxel model in case we
wanted to create grids for modelling. In this case, let's add a scalar field
for bone density noting:


.. code-block:: default

    voxels["density"] = np.full(voxels.n_cells, 3.65) # g/cc
    voxels






.. only:: builder_html

    .. raw:: html

        <table><tr><th>Header</th><th>Data Arrays</th></tr><tr><td>
        <table>
        <tr><th>UnstructuredGrid</th><th>Information</th></tr>
        <tr><td>N Cells</td><td>93041</td></tr>
        <tr><td>N Points</td><td>113192</td></tr>
        <tr><td>X Bounds</td><td>-5.633e+00, 5.584e+00</td></tr>
        <tr><td>Y Bounds</td><td>-1.860e+00, 1.858e+00</td></tr>
        <tr><td>Z Bounds</td><td>-2.125e+00, 2.097e+00</td></tr>
        <tr><td>N Arrays</td><td>3</td></tr>
        </table>

        </td><td>
        <table>
        <tr><th>Name</th><th>Field</th><th>Type</th><th>N Comp</th><th>Min</th><th>Max</th></tr>
        <tr><td>vtkOriginalPointIds</td><td>Points</td><td>int64</td><td>1</td><td>3.685e+03</td><td>7.283e+05</td></tr>
        <tr><td><b>vtkOriginalCellIds</b></td><td>Cells</td><td>int64</td><td>1</td><td>3.624e+03</td><td>7.017e+05</td></tr>
        <tr><td>density</td><td>Cells</td><td>float64</td><td>1</td><td>3.650e+00</td><td>3.650e+00</td></tr>
        </table>

        </td></tr> </table>
        <br />
        <br />


.. code-block:: default

    voxels.plot(scalars="density", cpos=cpos)





.. image:: /examples/01-filter/images/sphx_glr_voxelize_003.png
    :alt: voxelize
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(7.656346967151718, -9.802071079151158, -11.021236183314311),
     (0.2224512272564101, -0.4594554282112895, 0.5549738359311297),
     (-0.6279216753504943, -0.7513057097368636, 0.20311105371647395)]



A constant scalar field is kind of boring, so let's get a little fancier by
added a scalar field that varies by the distance from the bounding surface.


.. code-block:: default

    voxels.compute_implicit_distance(surface, inplace=True)
    voxels






.. only:: builder_html

    .. raw:: html

        <table><tr><th>Header</th><th>Data Arrays</th></tr><tr><td>
        <table>
        <tr><th>UnstructuredGrid</th><th>Information</th></tr>
        <tr><td>N Cells</td><td>93041</td></tr>
        <tr><td>N Points</td><td>113192</td></tr>
        <tr><td>X Bounds</td><td>-5.633e+00, 5.584e+00</td></tr>
        <tr><td>Y Bounds</td><td>-1.860e+00, 1.858e+00</td></tr>
        <tr><td>Z Bounds</td><td>-2.125e+00, 2.097e+00</td></tr>
        <tr><td>N Arrays</td><td>4</td></tr>
        </table>

        </td><td>
        <table>
        <tr><th>Name</th><th>Field</th><th>Type</th><th>N Comp</th><th>Min</th><th>Max</th></tr>
        <tr><td>vtkOriginalPointIds</td><td>Points</td><td>int64</td><td>1</td><td>3.685e+03</td><td>7.283e+05</td></tr>
        <tr><td>implicit_distance</td><td>Points</td><td>float64</td><td>1</td><td>-6.951e-01</td><td>4.148e-01</td></tr>
        <tr><td>vtkOriginalCellIds</td><td>Cells</td><td>int64</td><td>1</td><td>3.624e+03</td><td>7.017e+05</td></tr>
        <tr><td><b>density</b></td><td>Cells</td><td>float64</td><td>1</td><td>3.650e+00</td><td>3.650e+00</td></tr>
        </table>

        </td></tr> </table>
        <br />
        <br />


.. code-block:: default

    contours = voxels.contour(6, scalars="implicit_distance")

    p = pv.Plotter()
    p.add_mesh(voxels, opacity=0.25, scalars="implicit_distance")
    p.add_mesh(contours, opacity=0.5, scalars="implicit_distance")
    p.show(cpos=cpos)



.. image:: /examples/01-filter/images/sphx_glr_voxelize_004.png
    :alt: voxelize
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(7.656346967151718, -9.802071079151158, -11.021236183314311),
     (0.2224512272564101, -0.4594554282112895, 0.5549738359311297),
     (-0.6279216753504943, -0.7513057097368636, 0.20311105371647395)]




.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  20.067 seconds)


.. _sphx_glr_download_examples_01-filter_voxelize.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download sphx-glr-download-python

     :download:`Download Python source code: voxelize.py <voxelize.py>`



  .. container:: sphx-glr-download sphx-glr-download-jupyter

     :download:`Download Jupyter notebook: voxelize.ipynb <voxelize.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
