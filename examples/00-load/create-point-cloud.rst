.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_examples_00-load_create-point-cloud.py>`     to download the full example code
    .. rst-class:: sphx-glr-example-title

    .. _sphx_glr_examples_00-load_create-point-cloud.py:


.. _create_point_cloud:

Create Point Cloud
~~~~~~~~~~~~~~~~~~

Create a :class:`pyvista.PolyData` object from a point cloud of vertices and
scalar arrays for those points.



.. code-block:: default


    import numpy as np
    import pyvista as pv
    from pyvista import examples









Point clouds are generally constructed in the :class:`pyvista.PolyData` class
and can easiy have scalar/vector data arrays associated with the point
cloud. In this example, we'll work a bit backwards using a point cloud that
that is available from our ``examples`` module. This however is no different
than creating a PyVista mesh with your own NumPy arrays of vertice locations.


.. code-block:: default


    # Define some helpers - ignore these and use your own data!
    def generate_points(subset=0.02):
        """A helper to make a 3D NumPy array of points (n_points by 3)"""
        dataset = examples.download_lidar()
        ids = np.random.randint(low=0, high=dataset.n_points-1,
                                size=int(dataset.n_points * subset))
        return dataset.points[ids]


    points = generate_points()
    # Print first 5 rows to prove its a numpy array (n_points by 3)
    # Columns are (X Y Z)
    points[0:5, :]





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    pyvista_ndarray([[4.81077175e+05, 4.40010530e+06, 1.76079004e+03],
                     [4.81115975e+05, 4.40008490e+06, 1.77026001e+03],
                     [4.81017475e+05, 4.40009640e+06, 1.76232996e+03],
                     [4.81112875e+05, 4.40018030e+06, 1.76943994e+03],
                     [4.81105575e+05, 4.40016820e+06, 1.75900000e+03]])



Now that you have a NumPy array of points/vertices either from our sample
data or your own project, creating a PyVista mesh of those points is simply:


.. code-block:: default

    point_cloud = pv.PolyData(points)
    point_cloud






.. only:: builder_html

    .. raw:: html


        <table>
        <tr><th>PolyData</th><th>Information</th></tr>
        <tr><td>N Cells</td><td>67841</td></tr>
        <tr><td>N Points</td><td>67841</td></tr>
        <tr><td>X Bounds</td><td>4.809e+05, 4.811e+05</td></tr>
        <tr><td>Y Bounds</td><td>4.400e+06, 4.400e+06</td></tr>
        <tr><td>Z Bounds</td><td>1.754e+03, 1.785e+03</td></tr>
        <tr><td>N Arrays</td><td>0</td></tr>
        </table>


        <br />
        <br />

And we can even do a sanity check


.. code-block:: default

    np.allclose(points, point_cloud.points)





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    True



And now that we have a PyVista mesh, we can plot it. Note that we add an
option to use eye dome lighting - this is a shading technique to improve
depth perception with point clouds (learn more in :ref:`ref_edl`).


.. code-block:: default

    point_cloud.plot(eye_dome_lighting=True)




.. image:: /examples/00-load/images/sphx_glr_create-point-cloud_001.png
    :alt: create point cloud
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(481322.05453167664, 4400455.17953138, 2062.934536582394),
     (481028.37499997707, 4400161.49999968, 1769.2550048828125),
     (0.0, 0.0, 1.0)]



Now what if you have data attributes (scalar/vector arrays) that you'd like
to associate with every node of your mesh? You can easily add NumPy data
arrays that have a length equal to the number of points in the mesh along the
first axis. For example, lets add a few arrays to this new ``point_cloud``
mesh.

Make an array of scalar values with the same length as the points array.
Each element in this array will correspond to points at the same index:


.. code-block:: default


    # Make data array using z-component of points array
    data = points[:,-1]

    # Add that data to the mesh with the name "uniform dist"
    point_cloud["elevation"] = data








And now we can plot the point cloud with that random data. PyVista is smart
enough to plot the scalar array you added by default. Note that this time,
we specify to render every point as its own sphere.


.. code-block:: default

    point_cloud.plot(render_points_as_spheres=True)




.. image:: /examples/00-load/images/sphx_glr_create-point-cloud_002.png
    :alt: create point cloud
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(481322.05453167664, 4400455.17953138, 2062.934536582394),
     (481028.37499997707, 4400161.49999968, 1769.2550048828125),
     (0.0, 0.0, 1.0)]



That data is kind of boring, right? You can also add data arrays with
more than one scalar value - perhaps a vector with three elements? Let's
make a little function that will compute vectors for every node in the point
cloud and add those vectors to the mesh.

This time, we're going to create a totally new, random point cloud.


.. code-block:: default


    # Create random XYZ points
    points = np.random.rand(100, 3)
    # Make PolyData
    point_cloud = pv.PolyData(points)


    def compute_vectors(mesh):
        origin = mesh.center
        vectors = mesh.points - origin
        vectors = vectors / np.linalg.norm(vectors, axis=1)[:, None]
        return vectors

    vectors = compute_vectors(point_cloud)
    vectors[0:5, :]





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    pyvista_ndarray([[ 0.94527418,  0.14377323,  0.29289244],
                     [-0.55338671, -0.82211611,  0.13374699],
                     [ 0.42270726, -0.0942241 ,  0.90135475],
                     [ 0.18796832, -0.7228277 , -0.6649722 ],
                     [ 0.27461999,  0.43989808, -0.85502839]])




.. code-block:: default


    point_cloud['vectors'] = vectors








Now we can make arrows using those vectors using the glyph filter
(see :ref:`glyph_example` for more details).


.. code-block:: default


    arrows = point_cloud.glyph(orient='vectors', scale=False, factor=0.15,)

    # Display the arrows
    plotter = pv.Plotter()
    plotter.add_mesh(point_cloud, color='maroon', point_size=10.,
                     render_points_as_spheres=True)
    plotter.add_mesh(arrows, color='lightblue')
    # plotter.add_point_labels([point_cloud.center,], ['Center',],
    #                          point_color='yellow', point_size=20)
    plotter.show_grid()
    plotter.show()



.. image:: /examples/00-load/images/sphx_glr_create-point-cloud_003.png
    :alt: create point cloud
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(2.8755509194513036, 2.873390604980774, 2.8402768161674214),
     (0.5149582028388977, 0.5127978883683681, 0.47968409955501556),
     (0.0, 0.0, 1.0)]




.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  10.468 seconds)


.. _sphx_glr_download_examples_00-load_create-point-cloud.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download sphx-glr-download-python

     :download:`Download Python source code: create-point-cloud.py <create-point-cloud.py>`



  .. container:: sphx-glr-download sphx-glr-download-jupyter

     :download:`Download Jupyter notebook: create-point-cloud.ipynb <create-point-cloud.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
