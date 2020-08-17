.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_examples_00-load_create-structured-surface.py>`     to download the full example code
    .. rst-class:: sphx-glr-example-title

    .. _sphx_glr_examples_00-load_create-structured-surface.py:


.. _ref_create_structured:

Creating a Structured Surface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a StructuredGrid surface from NumPy arrays


.. code-block:: default


    # sphinx_gallery_thumbnail_number = 2
    import pyvista as pv
    from pyvista import examples
    import numpy as np









From NumPy Meshgrid
+++++++++++++++++++

Create a simple meshgrid using NumPy


.. code-block:: default


    # Make data
    x = np.arange(-10, 10, 0.25)
    y = np.arange(-10, 10, 0.25)
    x, y = np.meshgrid(x, y)
    r = np.sqrt(x ** 2 + y ** 2)
    z = np.sin(r)








Now pass the NumPy meshgrid to PyVista


.. code-block:: default


    # Create and plot structured grid
    grid = pv.StructuredGrid(x, y, z)
    grid.plot()




.. image:: /examples/00-load/images/sphx_glr_create-structured-surface_001.png
    :alt: create structured surface
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(31.107430113485155, 31.107430113485155, 31.232431754442583),
     (-0.125, -0.125, 1.6409574268849703e-06),
     (0.0, 0.0, 1.0)]




.. code-block:: default


    # Plot mean curvature as well
    grid.plot_curvature(clim=[-1, 1])




.. image:: /examples/00-load/images/sphx_glr_create-structured-surface_002.png
    :alt: create structured surface
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(31.107430113485155, 31.107430113485155, 31.232431754442583),
     (-0.125, -0.125, 1.6409574268849703e-06),
     (0.0, 0.0, 1.0)]



Generating a structured grid is a one liner in this module, and the points
from the resulting surface can be accessed as a NumPy array:


.. code-block:: default


    grid.points






.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    pyvista_ndarray([[-10.        , -10.        ,   0.99998766],
                     [-10.        ,  -9.75      ,   0.98546793],
                     [-10.        ,  -9.5       ,   0.9413954 ],
                     ...,
                     [  9.75      ,   9.25      ,   0.76645876],
                     [  9.75      ,   9.5       ,   0.86571785],
                     [  9.75      ,   9.75      ,   0.93985707]])



From XYZ Points
+++++++++++++++

Quite often, you might be given a set of coordinates (XYZ points) in a simple
tabular format where there exists some structure such that grid could be
built between the nodes you have. A great example is found in
`pyvista-support#16`_ where a structured grid that is rotated from the
cartesian reference frame is given as just XYZ points. In these cases, all
that is needed to recover the grid is the dimensions of the grid
(`nx` by `ny` by `nz`) and that the coordinates are ordered appropriately.

.. _pyvista-support#16: https://github.com/pyvista/pyvista-support/issues/16

For this example, we will create a small dataset and rotate the
coordinates such that they are not on orthogonal to cartesian reference
frame.


.. code-block:: default



    def make_point_set():
        """Ignore the contents of this function. Just know that it returns an
        n by 3 numpy array of structured coordinates."""
        n, m = 29, 32
        x = np.linspace(-200, 200, num=n) + np.random.uniform(-5, 5, size=n)
        y = np.linspace(-200, 200, num=m) + np.random.uniform(-5, 5, size=m)
        xx, yy = np.meshgrid(x, y)
        A, b = 100, 100
        zz = A * np.exp(-0.5 * ((xx / b) ** 2.0 + (yy / b) ** 2.0))
        points = np.c_[xx.reshape(-1), yy.reshape(-1), zz.reshape(-1)]
        foo = pv.PolyData(points)
        foo.rotate_z(36.6)
        return foo.points


    # Get the points as a 2D NumPy array (N by 3)
    points = make_point_set()
    points[0:5, :]





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    pyvista_ndarray([[ -38.4079378 , -280.25137899,    1.83009876],
                     [ -31.29978162, -274.97239633,    2.17210215],
                     [ -20.8237589 , -267.19221524,    2.75634285],
                     [  -2.235506  , -253.38736034,    4.03361337],
                     [   3.64885712, -249.01724661,    4.49976432]])



Now pretend that the (n by 3) NumPy array above are coordinates that you
have, possibly from a file with three columns of XYZ points.

We simply need to recover the dimensions of the grid that these points make
and then we can generate a :class:`pyvista.StructuredGrid` mesh.

Let's preview the points to see what we are dealing with:


.. code-block:: default

    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 10))
    plt.scatter(points[:, 0], points[:, 1], c=points[:, 2])
    plt.axis("image")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.show()




.. image:: /examples/00-load/images/sphx_glr_create-structured-surface_003.png
    :alt: create structured surface
    :class: sphx-glr-single-img





In the figure above, we can see some inherit structure to the points and thus
we could connect the points as a structured grid. All we need to know are the
dimensions of the grid present. In this case, we know (because we made this
dataset) the dimensions are ``[29, 32, 1]``, but you might not know the
dimensions of your pointset. There are a few ways to figure out the
dimensionality of structured grid including:

* manually counting the nodes along the edges of the pointset
* using a technique like principle component analysis to strip the rotation from the dataset and count the unique values along each axis for the new;y projected dataset.


.. code-block:: default


    # Once you've figured out your grid's dimensions, simple create the
    # :class:`pyvista.StructuredGrid` as follows:

    mesh = pv.StructuredGrid()
    # Set the coordinates from the numpy array
    mesh.points = points
    # set the dimensions
    mesh.dimensions = [29, 32, 1]

    # and then inspect it!
    mesh.plot(show_edges=True, show_grid=True, cpos="xy")





.. image:: /examples/00-load/images/sphx_glr_create-structured-surface_004.png
    :alt: create structured surface
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(0.5084344296064103, 1.751391624615792, 1601.1345952203399),
     (0.5084344296064103, 1.751391624615792, 50.74624238018185),
     (0.0, 1.0, 0.0)]



Extending a 2D StructuredGrid to 3D
+++++++++++++++++++++++++++++++++++

A 2D :class:`pyvista.StructuredGrid` mesh can be extended into a 3D mesh.
This is highly applicable when wanting to create a terrain following mesh
in earth science research applications.

For example, we could have a :class:`pyvista.StructuredGrid` of a topography
surface and extend that surface to a few different levels and connect each
"level" to create the 3D terrain following mesh.

Let's start with a simple example by extending the wave mesh to 3D


.. code-block:: default

    struct = examples.load_structured()
    struct.plot(show_edges=True)




.. image:: /examples/00-load/images/sphx_glr_create-structured-surface_005.png
    :alt: create structured surface
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(31.107430113485155, 31.107430113485155, 31.232431754442583),
     (-0.125, -0.125, 1.6409574268849703e-06),
     (0.0, 0.0, 1.0)]




.. code-block:: default

    top = struct.points.copy()
    bottom = struct.points.copy()
    bottom[:,-1] = -10.0 # Wherever you want the plane

    vol = pv.StructuredGrid()
    vol.points = np.vstack((top, bottom))
    vol.dimensions = [*struct.dimensions[0:2], 2]
    vol.plot(show_edges=True)



.. image:: /examples/00-load/images/sphx_glr_create-structured-surface_006.png
    :alt: create structured surface
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(33.35655554014341, 33.35655554014341, 28.98155188746257),
     (-0.125, -0.125, -4.500003652680841),
     (0.0, 0.0, 1.0)]




.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  8.084 seconds)


.. _sphx_glr_download_examples_00-load_create-structured-surface.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download sphx-glr-download-python

     :download:`Download Python source code: create-structured-surface.py <create-structured-surface.py>`



  .. container:: sphx-glr-download sphx-glr-download-jupyter

     :download:`Download Jupyter notebook: create-structured-surface.ipynb <create-structured-surface.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
