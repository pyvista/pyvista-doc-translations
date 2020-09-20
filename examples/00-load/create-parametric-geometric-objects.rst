.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_examples_00-load_create-parametric-geometric-objects.py>`     to download the full example code
    .. rst-class:: sphx-glr-example-title

    .. _sphx_glr_examples_00-load_create-parametric-geometric-objects.py:


.. _ref_parametric_example:

Parametric Geometric Objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creating parametric objects


.. code-block:: default


    # sphinx_gallery_thumbnail_number = 12
    import pyvista as pv
    from math import pi








This example demonstrates how to plot parametric objects using pyvista

Supertoroid
+++++++++++


.. code-block:: default


    supertoroid = pv.ParametricSuperToroid(n1=0.5)
    supertoroid.plot(color="tan", smooth_shading=True)




.. image:: /examples/00-load/images/sphx_glr_create-parametric-geometric-objects_001.png
    :alt: create parametric geometric objects
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(4.861252979770378, 4.8614418072850265, 4.861252979770378),
     (0.0, 0.0001888275146484375, 0.0),
     (0.0, 0.0, 1.0)]



Parametric Ellipsoid
++++++++++++++++++++


.. code-block:: default


    # Ellipsoid with a long x axis
    ellipsoid = pv.ParametricEllipsoid(10, 5, 5)
    ellipsoid.plot(color="tan")





.. image:: /examples/00-load/images/sphx_glr_create-parametric-geometric-objects_002.png
    :alt: create parametric geometric objects
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(27.312485178198028, 27.312485178198028, 27.315001924719024),
     (0.0, 0.0, 0.0025167465209960938),
     (0.0, 0.0, 1.0)]



Partial Parametric Ellipsoid
++++++++++++++++++++++++++++


.. code-block:: default


    # cool plotting direction
    cpos = [
        (21.9930, 21.1810, -30.3780),
        (-1.1640, -1.3098, -0.1061),
        (0.8498, -0.2515, 0.4631),
    ]


    # half ellipsoid
    part_ellipsoid = pv.ParametricEllipsoid(10, 5, 5, max_v=pi / 2)
    part_ellipsoid.plot(color="tan", smooth_shading=True, cpos=cpos)





.. image:: /examples/00-load/images/sphx_glr_create-parametric-geometric-objects_003.png
    :alt: create parametric geometric objects
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(21.993, 21.181, -30.378),
     (-1.164, -1.3098, -0.1061),
     (0.8498535849578507, -0.2515158585748405, 0.4631292012167341)]



Pseudosphere
++++++++++++


.. code-block:: default


    pseudosphere = pv.ParametricPseudosphere()
    pseudosphere.plot(color="tan", smooth_shading=True)




.. image:: /examples/00-load/images/sphx_glr_create-parametric-geometric-objects_004.png
    :alt: create parametric geometric objects
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(9.462755175257607, 9.462755175257607, 9.462503792668267),
     (0.0, 0.0, -0.00025138258934020996),
     (0.0, 0.0, 1.0)]



Bohemian Dome
+++++++++++++


.. code-block:: default



    bohemiandome = pv.ParametricBohemianDome()
    bohemiandome.plot(color="tan")




.. image:: /examples/00-load/images/sphx_glr_create-parametric-geometric-objects_005.png
    :alt: create parametric geometric objects
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(5.110157436636874, 5.109779841212222, 5.11003156652827),
     (0.0, -0.0003775954246520996, -0.00012587010860443115),
     (0.0, 0.0, 1.0)]



Bour
++++


.. code-block:: default


    bour = pv.ParametricBour()
    bour.plot(color="tan")




.. image:: /examples/00-load/images/sphx_glr_create-parametric-geometric-objects_006.png
    :alt: create parametric geometric objects
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(4.841760795218481, 4.844779532057776, 4.470163982016577),
     (-0.0030187368392944336, 0.0, -0.37461555004119873),
     (0.0, 0.0, 1.0)]



Boy's Surface
+++++++++++++


.. code-block:: default


    boy = pv.ParametricBoy()
    boy.plot(color="tan")




.. image:: /examples/00-load/images/sphx_glr_create-parametric-geometric-objects_007.png
    :alt: create parametric geometric objects
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(2.864744569020921, 3.3467303764397442, 3.496735627608949),
     (-0.4821150302886963, -0.00012922286987304688, 0.14987602829933167),
     (0.0, 0.0, 1.0)]



Catalan Minimal
+++++++++++++++


.. code-block:: default


    catalanminimal = pv.ParametricCatalanMinimal()
    catalanminimal.plot(color="tan")




.. image:: /examples/00-load/images/sphx_glr_create-parametric-geometric-objects_008.png
    :alt: create parametric geometric objects
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(31.542660237102616, 32.54206812456142, 31.542660237102616),
     (0.0, 0.9994078874588013, 0.0),
     (0.0, 0.0, 1.0)]



Conic Spiral
++++++++++++


.. code-block:: default


    conicspiral = pv.ParametricConicSpiral()
    conicspiral.plot(color="tan")




.. image:: /examples/00-load/images/sphx_glr_create-parametric-geometric-objects_009.png
    :alt: create parametric geometric objects
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(1.4978023605683783, 1.947848475191925, 1.9472122701147536),
     (-0.4000125899910927, 0.05003352463245392, 0.04939731955528259),
     (0.0, 0.0, 1.0)]



Cross Cap
+++++++++


.. code-block:: default


    crosscap = pv.ParametricCrossCap()
    crosscap.plot(color="tan")




.. image:: /examples/00-load/images/sphx_glr_create-parametric-geometric-objects_010.png
    :alt: create parametric geometric objects
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(3.8626410496722956, 3.8628927898895045, 3.8628927898895045),
     (-0.0002517402172088623, 0.0, 0.0),
     (0.0, 0.0, 1.0)]



Dini
++++


.. code-block:: default


    dini = pv.ParametricDini()
    dini.plot(color="tan")




.. image:: /examples/00-load/images/sphx_glr_create-parametric-geometric-objects_011.png
    :alt: create parametric geometric objects
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(12.702617897617449, 10.672241344081987, 10.672493054496874),
     (2.0303765535354614, 0.0, 0.0002517104148864746),
     (0.0, 0.0, 1.0)]



Enneper
+++++++


.. code-block:: default


    enneper = pv.ParametricEnneper()
    enneper.plot(cpos="yz")




.. image:: /examples/00-load/images/sphx_glr_create-parametric-geometric-objects_012.png
    :alt: create parametric geometric objects
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(42.946638627281644, 0.0, 0.0),
     (0.0, 0.0, 0.0),
     (0.0, 0.0, 1.0)]



Figure-8 Klein
++++++++++++++


.. code-block:: default


    figure8klein = pv.ParametricFigure8Klein()
    figure8klein.plot()




.. image:: /examples/00-load/images/sphx_glr_create-parametric-geometric-objects_013.png
    :alt: create parametric geometric objects
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(6.241280195618312, 6.241271850968044, 6.471927580738704),
     (0.0, -8.344650268554688e-06, 0.23064738512039185),
     (0.0, 0.0, 1.0)]



Henneberg
+++++++++


.. code-block:: default


    henneberg = pv.ParametricHenneberg()
    henneberg.plot(color="tan")




.. image:: /examples/00-load/images/sphx_glr_create-parametric-geometric-objects_014.png
    :alt: create parametric geometric objects
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(30.00610627059714, 30.004212273404757, 30.004212273404757),
     (0.0018939971923828125, 0.0, 0.0),
     (0.0, 0.0, 1.0)]



Klein
+++++


.. code-block:: default


    klein = pv.ParametricKlein()
    klein.plot(color="tan")




.. image:: /examples/00-load/images/sphx_glr_create-parametric-geometric-objects_015.png
    :alt: create parametric geometric objects
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(6.208944243443206, 8.311908167851165, 6.361395341408446),
     (0.0, 2.102963924407959, 0.15245109796524048),
     (0.0, 0.0, 1.0)]



Kuen
++++


.. code-block:: default


    kuen = pv.ParametricKuen()
    kuen.plot(color="tan")




.. image:: /examples/00-load/images/sphx_glr_create-parametric-geometric-objects_016.png
    :alt: create parametric geometric objects
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(6.381237118491877, 6.867912738570918, 6.381237118491877),
     (0.0, 0.4866756200790405, 0.0),
     (0.0, 0.0, 1.0)]



Mobius
++++++


.. code-block:: default


    mobius = pv.ParametricMobius()
    mobius.plot(color="tan")




.. image:: /examples/00-load/images/sphx_glr_create-parametric-geometric-objects_017.png
    :alt: create parametric geometric objects
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(5.656253052433871, 5.208850753983401, 5.656253052433871),
     (0.0, -0.44740229845046997, 0.0),
     (0.0, 0.0, 1.0)]



Plucker Conoid
++++++++++++++


.. code-block:: default


    pluckerconoid = pv.ParametricPluckerConoid()
    pluckerconoid.plot(color="tan")





.. image:: /examples/00-load/images/sphx_glr_create-parametric-geometric-objects_018.png
    :alt: create parametric geometric objects
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(9.721636447629232, 9.722391638478536, 9.721636447629232),
     (0.0, 0.0007551908493041992, 0.0),
     (0.0, 0.0, 1.0)]



Random Hills
++++++++++++


.. code-block:: default


    randomhills = pv.ParametricRandomHills()
    randomhills.plot(color="tan")




.. image:: /examples/00-load/images/sphx_glr_create-parametric-geometric-objects_019.png
    :alt: create parametric geometric objects
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(28.78004574694181, 42.59238058247112, 32.59238058247114),
     (-3.8123348355293274, 9.99999999999999, 0.0),
     (0.0, 0.0, 1.0)]



Roman
+++++


.. code-block:: default


    roman = pv.ParametricRoman()
    roman.plot(color="tan")




.. image:: /examples/00-load/images/sphx_glr_create-parametric-geometric-objects_020.png
    :alt: create parametric geometric objects
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(1.9315274394739659, 1.9315274394739659, 1.9315274394739659),
     (0.0, 0.0, 0.0),
     (0.0, 0.0, 1.0)]



Super Ellipsoid
+++++++++++++++


.. code-block:: default


    superellipsoid = pv.ParametricSuperEllipsoid(n1=0.1, n2=2)
    superellipsoid.plot(color="tan")




.. image:: /examples/00-load/images/sphx_glr_create-parametric-geometric-objects_021.png
    :alt: create parametric geometric objects
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(3.862698576895865, 3.862195245473059, 3.862698576895865),
     (0.0, -0.0005033314228057861, 0.0),
     (0.0, 0.0, 1.0)]



Torus
+++++


.. code-block:: default


    torus = pv.ParametricTorus()
    torus.plot(color="tan")




.. image:: /examples/00-load/images/sphx_glr_create-parametric-geometric-objects_022.png
    :alt: create parametric geometric objects
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(4.860818223814616, 4.861195819239268, 4.860818223814616),
     (0.0, 0.0003775954246520996, 0.0),
     (0.0, 0.0, 1.0)]



Circular Arc
++++++++++++


.. code-block:: default


    pointa = [-1, 0, 0]
    pointb = [0, 1, 0]
    center = [0, 0, 0]
    resolution = 100

    arc = pv.CircularArc(pointa, pointb, center, resolution)

    pl = pv.Plotter()
    pl.add_mesh(arc, color='k', line_width=4)
    pl.show_bounds()
    pl.view_xy()
    pl.show()





.. image:: /examples/00-load/images/sphx_glr_create-parametric-geometric-objects_023.png
    :alt: create parametric geometric objects
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(-0.5000000000499987, 0.5, 2.7320508074322785),
     (-0.5000000000499987, 0.5, 0.0),
     (0.0, 1.0, 0.0)]



Extruded Half Arc
+++++++++++++++++


.. code-block:: default


    pointa = [-1, 0, 0]
    pointb = [1, 0, 0]
    center = [0, 0, 0]
    resolution = 100

    arc = pv.CircularArc(pointa, pointb, center, resolution)
    poly = arc.extrude([0, 0, 1])
    poly.plot(color="tan", cpos='iso', show_edges=True)



.. image:: /examples/00-load/images/sphx_glr_create-parametric-geometric-objects_024.png
    :alt: create parametric geometric objects
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(2.7320508075688776, 2.2320508075688776, 3.2320508075688776),
     (0.0, -0.5, 0.5),
     (0.0, 0.0, 1.0)]




.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  18.532 seconds)


.. _sphx_glr_download_examples_00-load_create-parametric-geometric-objects.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download sphx-glr-download-python

     :download:`Download Python source code: create-parametric-geometric-objects.py <create-parametric-geometric-objects.py>`



  .. container:: sphx-glr-download sphx-glr-download-jupyter

     :download:`Download Jupyter notebook: create-parametric-geometric-objects.ipynb <create-parametric-geometric-objects.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
