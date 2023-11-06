

.. _sphx_glr_examples_03-widgets:

.. _widgets:

Widgets
-------

PyVista has several widgets that can be added to the rendering scene to control
filters like clipping, slicing, and thresholding - specifically there are
widgets to control the positions of boxes, planes, and lines or slider bars
which can all be highly customized through the use of custom callback
functions.

Here we'll take a look at the various widgets, some helper methods that leverage
those widgets to do common tasks, and demonstrate how to leverage the widgets
for user defined tasks and processing routines.



.. raw:: html

    <div class="sphx-glr-thumbnails">


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example demonstrates how to create a simple animation. A timer is used to move a sphere ac...">

.. only:: html

  .. image:: /examples/03-widgets/images/thumb/sphx_glr_animation_thumb.png
    :alt:

  :ref:`sphx_glr_examples_03-widgets_animation.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Animation</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The box widget can be enabled and disabled by the pyvista.Plotter.add_box_widget and pyvista.Pl...">

.. only:: html

  .. image:: /examples/03-widgets/images/thumb/sphx_glr_box-widget_thumb.png
    :alt:

  :ref:`sphx_glr_examples_03-widgets_box-widget.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Box Widget</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Use a checkbox to turn on/off the visibility of meshes in a scene.">

.. only:: html

  .. image:: /examples/03-widgets/images/thumb/sphx_glr_checkbox-widget_thumb.png
    :alt:

  :ref:`sphx_glr_examples_03-widgets_checkbox-widget.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Checkbox Widget</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Clip Volume Widget">

.. only:: html

  .. image:: /examples/03-widgets/images/thumb/sphx_glr_clip-volume_thumb.png
    :alt:

  :ref:`sphx_glr_examples_03-widgets_clip-volume.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Clip Volume Widget</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The line widget can be enabled and disabled by the pyvista.Plotter.add_line_widget and pyvista....">

.. only:: html

  .. image:: /examples/03-widgets/images/thumb/sphx_glr_line-widget_thumb.png
    :alt:

  :ref:`sphx_glr_examples_03-widgets_line-widget.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Line Widget</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Use a class based callback to track multiple slider widgets for updating a single mesh.">

.. only:: html

  .. image:: /examples/03-widgets/images/thumb/sphx_glr_multi-slider-widget_thumb.png
    :alt:

  :ref:`sphx_glr_examples_03-widgets_multi-slider-widget.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Multiple Slider Widgets</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The plane widget can be enabled and disabled by the pyvista.Plotter.add_plane_widget and pyvist...">

.. only:: html

  .. image:: /examples/03-widgets/images/thumb/sphx_glr_plane-widget_thumb.png
    :alt:

  :ref:`sphx_glr_examples_03-widgets_plane-widget.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Plane Widget</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The slider widget can be enabled and disabled by the pyvista.Plotter.add_slider_widget and pyvi...">

.. only:: html

  .. image:: /examples/03-widgets/images/thumb/sphx_glr_slider-bar-widget_thumb.png
    :alt:

  :ref:`sphx_glr_examples_03-widgets_slider-bar-widget.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Slider Bar Widget</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The sphere widget can be enabled and disabled by the pyvista.Plotter.add_sphere_widget and pyvi...">

.. only:: html

  .. image:: /examples/03-widgets/images/thumb/sphx_glr_sphere-widget_thumb.png
    :alt:

  :ref:`sphx_glr_examples_03-widgets_sphere-widget.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Sphere Widget</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip=" A spline widget can be enabled and disabled by the pyvista.Plotter.add_spline_widget and pyvis...">

.. only:: html

  .. image:: /examples/03-widgets/images/thumb/sphx_glr_spline-widget_thumb.png
    :alt:

  :ref:`sphx_glr_examples_03-widgets_spline-widget.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Spline Widget</div>
    </div>


.. raw:: html

    </div>


.. toctree::
   :hidden:

   /examples/03-widgets/animation
   /examples/03-widgets/box-widget
   /examples/03-widgets/checkbox-widget
   /examples/03-widgets/clip-volume
   /examples/03-widgets/line-widget
   /examples/03-widgets/multi-slider-widget
   /examples/03-widgets/plane-widget
   /examples/03-widgets/slider-bar-widget
   /examples/03-widgets/sphere-widget
   /examples/03-widgets/spline-widget
