
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "examples/99-advanced/atomic-orbitals.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        :ref:`Go to the end <sphx_glr_download_examples_99-advanced_atomic-orbitals.py>`
        to download the full example code

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_examples_99-advanced_atomic-orbitals.py:


.. _plot_atomic_orbitals_example:

Plot Atomic Orbitals
--------------------
Visualize the wave functions (orbitals) of the hydrogen atom.

.. GENERATED FROM PYTHON SOURCE LINES 11-24

Import
~~~~~~
Import the applicable libraries.

.. note::
   This example is modeled off of `Matplotlib: Hydrogen Wave Function
   <http://staff.ustc.edu.cn/~zqj/posts/Hydrogen-Wavefunction/>`_.

   This example requires `sympy <https://www.sympy.org/>`_. Install it with:

   .. code:: python

      pip install sympy

.. GENERATED FROM PYTHON SOURCE LINES 24-30

.. code-block:: default


    import numpy as np

    import pyvista as pv
    from pyvista import examples








.. GENERATED FROM PYTHON SOURCE LINES 31-57

Generate the Dataset
~~~~~~~~~~~~~~~~~~~~
Generate the dataset by evaluating the analytic hydrogen wave function from
``sympy``.

.. math::
   \begin{equation}
       \psi_{n\ell m}(r,\theta,\phi)
       =
       \sqrt{
           \left(\frac{2}{na_0}\right)^3\, \frac{(n-\ell-1)!}{2n[(n+\ell)!]}
       }
       e^{-r / na_0}
       \left(\frac{2r}{na_0}\right)^\ell
       L_{n-\ell-1}^{2\ell+1} \cdot Y_\ell^m(\theta, \phi)
   \end{equation}

See `Hydrogen atom <https://en.wikipedia.org/wiki/Hydrogen_atom>`_ for more
details.

This dataset evaluates this function for the hydrogen orbital
:math:`3d_{xy}`, with the following quantum numbers:

* Principal quantum number: ``n=3``
* Azimuthal quantum number: ``l=2``
* Magnetic quantum number: ``m=-2``

.. GENERATED FROM PYTHON SOURCE LINES 57-62

.. code-block:: default


    grid = examples.load_hydrogen_orbital(3, 2, -2)
    grid







.. raw:: html

    <div class="output_subarea output_html rendered_html output_result">
    <table style='width: 100%;'><tr><th>Header</th><th>Data Arrays</th></tr><tr><td>
    <table style='width: 100%;'>
    <tr><th>ImageData</th><th>Information</th></tr>
    <tr><td>N Cells</td><td>970299</td></tr>
    <tr><td>N Points</td><td>1000000</td></tr>
    <tr><td>X Bounds</td><td>-2.350e+01, 2.350e+01</td></tr>
    <tr><td>Y Bounds</td><td>-2.350e+01, 2.350e+01</td></tr>
    <tr><td>Z Bounds</td><td>-2.350e+01, 2.350e+01</td></tr>
    <tr><td>Dimensions</td><td>100, 100, 100</td></tr>
    <tr><td>Spacing</td><td>4.747e-01, 4.747e-01, 4.747e-01</td></tr>
    <tr><td>N Arrays</td><td>2</td></tr>
    </table>

    </td><td>
    <table style='width: 100%;'>
    <tr><th>Name</th><th>Field</th><th>Type</th><th>N Comp</th><th>Min</th><th>Max</th></tr>
    <tr><td><b>real_wf</b></td><td>Points</td><td>float64</td><td>1</td><td>-1.689e-02</td><td>1.689e-02</td></tr>
    <tr><td>wf</td><td>Points</td><td>complex128</td><td>1</td><td>-1.689e-02+1.353e-03j</td><td>1.689e-02+1.353e-03j</td></tr>
    </table>

    </td></tr> </table>
    </div>
    <br />
    <br />

.. GENERATED FROM PYTHON SOURCE LINES 63-75

Plot the Orbital
~~~~~~~~~~~~~~~~
Plot the orbital using :func:`add_volume() <pyvista.Plotter.add_volume>` and
using the default scalars contained in ``grid``, ``real_wf``. This way we
can plot more than just the probability of the electron, but also the phase
of the electron wave function.

.. note::
   Since the real value of evaluated wave function for this orbital varies
   between ``[-<value>, <value>]``, we cannot use the default opacity
   ``opacity='linear'``. Instead, we use ``[1, 0, 1]`` since we would like
   the opacity to be proportional to the absolute value of the scalars.

.. GENERATED FROM PYTHON SOURCE LINES 75-85

.. code-block:: default



    pl = pv.Plotter()
    vol = pl.add_volume(grid, cmap='magma', opacity=[1, 0, 1])
    vol.prop.interpolation_type = 'linear'
    pl.camera.zoom(2)
    pl.show_axes()
    pl.show()






.. image-sg:: /examples/99-advanced/images/sphx_glr_atomic-orbitals_001.png
   :alt: atomic orbitals
   :srcset: /examples/99-advanced/images/sphx_glr_atomic-orbitals_001.png
   :class: sphx-glr-single-img







.. GENERATED FROM PYTHON SOURCE LINES 90-99

Plot the Orbital Contours as an Isosurface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Generate the contour plot for the orbital by determining when the orbital
equals 10% the maximum value of the orbital. This effectively captures the
most likely locations of the electron for this orbital.

Note how we use the absolute value of the scalars when evaluating
:func:`contour() <pyvista.DataSetFilters.contour>` to capture where the
positive and negative phases cross ``eval_at``.

.. GENERATED FROM PYTHON SOURCE LINES 99-113

.. code-block:: default


    eval_at = grid['real_wf'].max() * 0.1
    contours = grid.contour(
        [eval_at],
        scalars=np.abs(grid['real_wf']),
        method='marching_cubes',
    )
    contours = contours.interpolate(grid)
    contours.plot(
        smooth_shading=True,
        show_scalar_bar=False,
    )









.. tab-set::



   .. tab-item:: Static Scene



            
     .. image-sg:: /examples/99-advanced/images/sphx_glr_atomic-orbitals_002.png
        :alt: atomic orbitals
        :srcset: /examples/99-advanced/images/sphx_glr_atomic-orbitals_002.png
        :class: sphx-glr-single-img
     


   .. tab-item:: Interactive Scene



       .. offlineviewer:: /home/runner/work/pyvista-doc-translations/pyvista-doc-translations/pyvista/doc/source/examples/99-advanced/images/sphx_glr_atomic-orbitals_002.vtksz






.. GENERATED FROM PYTHON SOURCE LINES 114-129

Volumetric Plot: Plot the Orbitals using RGBA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Let's now combine some of the best parts of the two above plots. The
volumetric plot is great for showing the probability of the "electron cloud"
orbitals, but the colormap doesn't quite match reality as well as the
isosurface plot.

For this example we're going to use an RGBA colormap to tightly control the
way the orbitals are plotted. For this, the opacity will be mapped to the
probability of the electron being at a location in the grid, which we can do
by taking the absolute value squared of the orbital's wave function. We can
set the color of the orbital based on the phase, which we can get simply
with ``orbital['real_wf'] < 0``.

Let's start with a simple one, the :math:`3p_z` orbital.

.. GENERATED FROM PYTHON SOURCE LINES 129-168

.. code-block:: default




    def plot_orbital(orbital, cpos='iso', clip_plane='x'):
        """Plot an electron orbital using an RGBA colormap."""
        neg_mask = orbital['real_wf'] < 0
        rgba = np.zeros((orbital.n_points, 4), np.uint8)
        rgba[neg_mask, 0] = 255
        rgba[~neg_mask, 1] = 255

        # normalize opacity
        opac = np.abs(orbital['real_wf']) ** 2
        opac /= opac.max()
        rgba[:, -1] = opac * 255

        orbital['plot_scalars'] = rgba

        pl = pv.Plotter()
        vol = pl.add_volume(
            orbital,
            scalars='plot_scalars',
        )
        vol.prop.interpolation_type = 'linear'
        if clip_plane:
            pl.add_volume_clip_plane(
                vol,
                normal=clip_plane,
                normal_rotation=False,
            )
        pl.camera_position = cpos
        pl.camera.zoom(1.5)
        pl.show_axes()
        return pl.show()


    hydro_orbital = examples.load_hydrogen_orbital(3, 1, 0)
    plot_orbital(hydro_orbital, clip_plane='-x')






.. image-sg:: /examples/99-advanced/images/sphx_glr_atomic-orbitals_003.png
   :alt: atomic orbitals
   :srcset: /examples/99-advanced/images/sphx_glr_atomic-orbitals_003.png
   :class: sphx-glr-single-img







.. GENERATED FROM PYTHON SOURCE LINES 173-175

Volumetric Plot: :math:`4d_{z^2}` orbital
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. GENERATED FROM PYTHON SOURCE LINES 175-180

.. code-block:: default


    hydro_orbital = examples.load_hydrogen_orbital(4, 2, 0)
    plot_orbital(hydro_orbital, clip_plane='-y')






.. image-sg:: /examples/99-advanced/images/sphx_glr_atomic-orbitals_004.png
   :alt: atomic orbitals
   :srcset: /examples/99-advanced/images/sphx_glr_atomic-orbitals_004.png
   :class: sphx-glr-single-img







.. GENERATED FROM PYTHON SOURCE LINES 185-187

Volumetric Plot: :math:`4d_{xz}` orbital
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. GENERATED FROM PYTHON SOURCE LINES 187-192

.. code-block:: default


    hydro_orbital = examples.load_hydrogen_orbital(4, 2, -1)
    plot_orbital(hydro_orbital, clip_plane='-y')






.. image-sg:: /examples/99-advanced/images/sphx_glr_atomic-orbitals_005.png
   :alt: atomic orbitals
   :srcset: /examples/99-advanced/images/sphx_glr_atomic-orbitals_005.png
   :class: sphx-glr-single-img







.. GENERATED FROM PYTHON SOURCE LINES 197-203

Plot an Orbital Using a Density Plot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We can also plot atomic orbitals using a 3D density plot. For this, we will
use :func:`numpy.random.choice` to sample all the points of our
:class:`pyvista.ImageData` based on the probability of the electron being
at that coordinate.

.. GENERATED FROM PYTHON SOURCE LINES 203-243

.. code-block:: default


    # Generate the orbital and sample based on the square of the probability of an
    # electron being within a particular volume of space.
    hydro_orbital = examples.load_hydrogen_orbital(4, 2, 0, zoom_fac=0.5)
    prob = np.abs(hydro_orbital['real_wf']) ** 2
    prob /= prob.sum()
    indices = np.random.default_rng().choice(hydro_orbital.n_points, 10000, p=prob)

    # add a small amount of noise to these coordinates to remove the "grid like"
    # structure present in the underlying ImageData
    points = hydro_orbital.points[indices]
    points += np.random.default_rng().random(points.shape) - 0.5

    # Create a point cloud and add the phase as the active scalars
    point_cloud = pv.PolyData(points)
    point_cloud['phase'] = hydro_orbital['real_wf'][indices] < 0

    # Turn the point cloud into individual spheres. We do this so we can improve
    # the plot by enabling surface space ambient occlusion (SSAO)
    dplot = point_cloud.glyph(
        geom=pv.Sphere(theta_resolution=8, phi_resolution=8), scale=False, orient=False
    )

    # be sure to enable SSAO here. This makes the "points" that are deeper within
    # the density plot darker.
    pl = pv.Plotter()
    pl.add_mesh(
        dplot,
        smooth_shading=True,
        show_scalar_bar=False,
        cmap=['red', 'green'],
        ambient=0.2,
    )
    pl.enable_ssao(radius=10)
    pl.enable_anti_aliasing()
    pl.camera.zoom(2)
    pl.background_color = 'w'
    pl.show()









.. tab-set::



   .. tab-item:: Static Scene



            
     .. image-sg:: /examples/99-advanced/images/sphx_glr_atomic-orbitals_006.png
        :alt: atomic orbitals
        :srcset: /examples/99-advanced/images/sphx_glr_atomic-orbitals_006.png
        :class: sphx-glr-single-img
     


   .. tab-item:: Interactive Scene



       .. offlineviewer:: /home/runner/work/pyvista-doc-translations/pyvista-doc-translations/pyvista/doc/source/examples/99-advanced/images/sphx_glr_atomic-orbitals_006.vtksz






.. GENERATED FROM PYTHON SOURCE LINES 244-247

Density Plot - Gaussian Points Representation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Finally, let's plot the same data using the "Gaussian points" representation.

.. GENERATED FROM PYTHON SOURCE LINES 247-260

.. code-block:: default




    point_cloud.plot(
        style='points_gaussian',
        render_points_as_spheres=False,
        point_size=3,
        emissive=True,
        background='k',
        show_scalar_bar=False,
        cpos='xz',
        zoom=2,
    )




.. image-sg:: /examples/99-advanced/images/sphx_glr_atomic-orbitals_007.png
   :alt: atomic orbitals
   :srcset: /examples/99-advanced/images/sphx_glr_atomic-orbitals_007.png
   :class: sphx-glr-single-img








.. rst-class:: sphx-glr-timing

   **Total running time of the script:** (0 minutes 22.361 seconds)


.. _sphx_glr_download_examples_99-advanced_atomic-orbitals.py:

.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-example




    .. container:: sphx-glr-download sphx-glr-download-python

      :download:`Download Python source code: atomic-orbitals.py <atomic-orbitals.py>`

    .. container:: sphx-glr-download sphx-glr-download-jupyter

      :download:`Download Jupyter notebook: atomic-orbitals.ipynb <atomic-orbitals.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
