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


    pyvista_ndarray([[4.81126575e+05, 4.40023770e+06, 1.77373999e+03],
                     [4.80946675e+05, 4.40012940e+06, 1.76279004e+03],
                     [4.81006475e+05, 4.40014160e+06, 1.76139001e+03],
                     [4.81037575e+05, 4.40016990e+06, 1.76013000e+03],
                     [4.81041175e+05, 4.40007730e+06, 1.77019995e+03]])



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
        <tr><td>Z Bounds</td><td>1.754e+03, 1.787e+03</td></tr>
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


    [(481322.34016867896, 4400455.465168381, 2064.305134522179),
     (481028.37499997707, 4400161.49999968, 1770.3399658203125),
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


    [(481322.34016867896, 4400455.465168381, 2064.305134522179),
     (481028.37499997707, 4400161.49999968, 1770.3399658203125),
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


    pyvista_ndarray([[ 0.59510722,  0.79441411, -0.12146444],
                     [-0.39225688, -0.27002098, -0.87933111],
                     [-0.11289469,  0.72386593, -0.68064154],
                     [-0.15094767, -0.98028453,  0.12750313],
                     [-0.55767689,  0.76118028,  0.33106051]])




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


    [(2.876946683283532, 2.870840217228616, 2.8559254326481467),
     (0.5086461678147316, 0.5025397017598152, 0.4876249171793461),
     (0.0, 0.0, 1.0)]




.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  8.700 seconds)


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
