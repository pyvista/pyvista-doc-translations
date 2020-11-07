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


    [(4.861253025523928, 4.861441853038577, 4.861253025523928),
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


    [(27.315001924719024, 27.312485178198028, 27.312485178198028),
     (0.0025167465209960938, 0.0, 0.0),
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


    [(9.462503792668267, 9.462755175257607, 9.462755175257607),
     (-0.00025138258934020996, 0.0, 0.0),
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


    [(5.110031624561594, 5.109779899245546, 5.110157494670198),
     (-0.00012587010860443115, -0.0003775954246520996, 0.0),
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


    [(4.470163982016577, 4.844779532057776, 4.84779826889707),
     (-0.37461555004119873, 0.0, 0.0030187368392944336),
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


    [(3.496735663209918, 3.346730412040713, 3.8289746279463794),
     (0.14987602829933167, -0.00012922286987304688, 0.4821149930357933),
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


    [(31.542660281331067, 32.54206828799916, 31.542660519749646),
     (0.0, 0.9994080066680908, 2.384185791015625e-07),
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


    [(1.947212285780989, 1.9478484759569992, 2.297827556216799),
     (0.04939731955528259, 0.050033509731292725, 0.4000125899910927),
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


    [(3.8628927898895045, 3.8628927302848597, 3.8631445301067133),
     (0.0, -5.960464477539063e-08, 0.0002517402172088623),
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


    [(10.672493040603099, 10.6722411811766, 8.641864776652751),
     (0.0002517104148864746, -1.4901161193847656e-07, -2.0303765535354614),
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


    [(6.471927580738704, 6.241271850968044, 6.241280195618312),
     (0.23064738512039185, -8.344650268554688e-06, 0.0),
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


    [(30.00421257084943, 30.00421209401227, 30.002318335238467),
     (0.0, -4.76837158203125e-07, -0.001894235610961914),
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


    [(6.361395375111999, 8.311908181557236, 6.208944455960693),
     (0.15245109796524048, 2.102963904410476, 1.7881393432617188e-07),
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


    [(6.381237188722924, 6.86791274919732, 6.381237188722924),
     (0.0, 0.48667556047439575, 0.0),
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


    [(5.656253133787988, 5.208850894942163, 5.656253252997278),
     (0.0, -0.4474022388458252, 1.1920928955078125e-07),
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


    [(9.721636508639419, 9.722391699488723, 9.72163638943013),
     (0.0, 0.0007551908493041992, -1.1920928955078125e-07),
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


    [(32.59238063266725, 42.5923804083449, 36.404716943411536),
     (0.0, 9.99999977567765, 3.8123363107442856),
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


    [(3.862698653641108, 3.862195322218302, 3.862698653641108),
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


    [(4.860818269572256, 4.861195864996908, 4.860818269572256),
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

   **Total running time of the script:** ( 0 minutes  14.816 seconds)


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
