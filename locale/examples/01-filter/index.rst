

.. _sphx_glr_examples_01-filter:

Filtering
---------

These examples show case various mesh analysis and filtering routines present
in the :ref:`filters_ref` module. Explore these demos to perform tasks such as:

* Slicing and cutting meshes
* Computing mesh properties like volume, area, and surface normals
* Mesh decimation
* Extract regions of one mesh using another mesh's surface
* Ray tracing through surface meshes
* Resampling and interpolating scalar/vector values across meshes
* Integrating a vector field to generate streamlines
* Smoothing surfaces



.. raw:: html

    <div class="sphx-glr-thumbnails">


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Perform boolean operations with closed (manifold) surfaces.">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_boolean-operations_thumb.png
    :alt: Boolean Operations

  :ref:`sphx_glr_examples_01-filter_boolean-operations.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Boolean Operations</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Extract the coordinates of the centers of all cells or faces in a mesh.">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_cell-centers_thumb.png
    :alt: Extract Cell Centers

  :ref:`sphx_glr_examples_01-filter_cell-centers.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Extract Cell Centers</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Clip any PyVista dataset by a pyvista.PolyData surface mesh using the pyvista.DataSetFilters.cl...">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_clipping-with-surface_thumb.png
    :alt: Clipping with a Surface

  :ref:`sphx_glr_examples_01-filter_clipping-with-surface.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Clipping with a Surface</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Clip/cut any dataset using using planes or boxes.">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_clipping_thumb.png
    :alt: Clipping with Planes & Boxes

  :ref:`sphx_glr_examples_01-filter_clipping.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Clipping with Planes & Boxes</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example use the pyvista.PolyDataFilters.collision filter to detect the faces from one sphe...">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_collisions_thumb.png
    :alt: Collision

  :ref:`sphx_glr_examples_01-filter_collisions.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Collision</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip=" Compute normals on a surface.">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_compute-normals_thumb.png
    :alt: Computing Surface Normals

  :ref:`sphx_glr_examples_01-filter_compute-normals.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Computing Surface Normals</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip=" Calculate mass properties such as the volume or area of datasets">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_compute-volume_thumb.png
    :alt: Volumetric Analysis

  :ref:`sphx_glr_examples_01-filter_compute-volume.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Volumetric Analysis</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Use the connectivity filter to remove noisy isosurfaces.">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_connectivity_thumb.png
    :alt: Connectivity

  :ref:`sphx_glr_examples_01-filter_connectivity.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Connectivity</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Generate iso-lines or -surfaces for the scalars of a surface or volume.">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_contouring_thumb.png
    :alt: Contouring

  :ref:`sphx_glr_examples_01-filter_contouring.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Contouring</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Decimate a mesh">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_decimate_thumb.png
    :alt: Decimation

  :ref:`sphx_glr_examples_01-filter_decimate.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Decimation</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Compute the average thickness between two surfaces.">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_distance-between-surfaces_thumb.png
    :alt: Distance Between Two Surfaces

  :ref:`sphx_glr_examples_01-filter_distance-between-surfaces.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Distance Between Two Surfaces</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Extract the cells in a mesh that exist inside or outside a closed surface of another mesh">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_extract-cells-inside-surface_thumb.png
    :alt: Extract Cells Inside Surface

  :ref:`sphx_glr_examples_01-filter_extract-cells-inside-surface.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Extract Cells Inside Surface</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Extract edges from a surface.">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_extract-edges_thumb.png
    :alt: Extract Edges

  :ref:`sphx_glr_examples_01-filter_extract-edges.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Extract Edges</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="You can extract the surface of nearly any object within pyvista using the extract_surface filte...">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_extract-surface_thumb.png
    :alt: Extract Surface

  :ref:`sphx_glr_examples_01-filter_extract-surface.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Extract Surface</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This takes polygonal data as input and generates polygonal data on output. The input dataset is...">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_extrude-rotate_thumb.png
    :alt: Extrude Rotation

  :ref:`sphx_glr_examples_01-filter_extrude-rotate.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Extrude Rotation</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Extrude Trim">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_extrude-trim_thumb.png
    :alt: Extrude Trim

  :ref:`sphx_glr_examples_01-filter_extrude-trim.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Extrude Trim</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Generate a surface from a scalar field using the flying edges and marching cubes filters as pro...">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_flying_edges_thumb.png
    :alt: Marching Cubes

  :ref:`sphx_glr_examples_01-filter_flying_edges.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Marching Cubes</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Perform a Gaussian convolution on a uniformly gridded data set.">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_gaussian-smoothing_thumb.png
    :alt: Gaussian Smoothing

  :ref:`sphx_glr_examples_01-filter_gaussian-smoothing.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Gaussian Smoothing</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Calculates the geodesic path between two vertices using Dijkstra&#x27;s algorithm">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_geodesic_thumb.png
    :alt: Geodesic Paths

  :ref:`sphx_glr_examples_01-filter_geodesic.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Geodesic Paths</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Use vectors in a dataset to plot and orient glyphs/geometric objects.">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_glyphs_thumb.png
    :alt: Plotting Glyphs (Vectors or PolyData)

  :ref:`sphx_glr_examples_01-filter_glyphs.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Plotting Glyphs (Vectors or PolyData)</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="vtk supports tables of glyphs from which glyphs are looked up. This example demonstrates this f...">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_glyphs_table_thumb.png
    :alt: Table of Glyphs

  :ref:`sphx_glr_examples_01-filter_glyphs_table.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Table of Glyphs</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Estimate the gradient of a scalar or vector field in a data set.">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_gradients_thumb.png
    :alt: Compute Gradients of a Field

  :ref:`sphx_glr_examples_01-filter_gradients.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Compute Gradients of a Field</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example shows how to apply a Fast Fourier Transform (FFT) to a pyvista.UniformGrid using p...">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_image-fft-perlin-noise_thumb.png
    :alt: Fast Fourier Transform with Perlin Noise

  :ref:`sphx_glr_examples_01-filter_image-fft-perlin-noise.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Fast Fourier Transform with Perlin Noise</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example shows how to apply a Fast Fourier Transform (FFT) to a pyvista.UniformGrid using p...">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_image-fft_thumb.png
    :alt: Fast Fourier Transform

  :ref:`sphx_glr_examples_01-filter_image-fft.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Fast Fourier Transform</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Integrate data over a surface using the pyvista.DataSetFilters.integrate_data filter.">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_integrate-data_thumb.png
    :alt: Integrate Data

  :ref:`sphx_glr_examples_01-filter_integrate-data.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Integrate Data</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Interpolate one mesh&#x27;s point/cell arrays onto another mesh&#x27;s nodes using a Gaussian Kernel.">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_interpolate_thumb.png
    :alt: Interpolating

  :ref:`sphx_glr_examples_01-filter_interpolate.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Interpolating</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Leverage powerful VTK algorithms for computing mesh quality.">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_mesh-quality_thumb.png
    :alt: Computing Mesh Quality

  :ref:`sphx_glr_examples_01-filter_mesh-quality.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Computing Mesh Quality</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Single line segment ray tracing for PolyData objects.">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_poly-ray-trace_thumb.png
    :alt: Ray Tracing

  :ref:`sphx_glr_examples_01-filter_poly-ray-trace.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Ray Tracing</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="pyvista.PolyData surfaces and pointsets can easily be projected to a plane defined by a normal ...">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_project-plane_thumb.png
    :alt: Project to a Plane

  :ref:`sphx_glr_examples_01-filter_project-plane.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Project to a Plane</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example reflects a mesh across a plane.">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_reflect_thumb.png
    :alt: Reflect Meshes

  :ref:`sphx_glr_examples_01-filter_reflect.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Reflect Meshes</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Resample one mesh&#x27;s point/cell arrays onto another mesh&#x27;s nodes.">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_resample_thumb.png
    :alt: Resampling

  :ref:`sphx_glr_examples_01-filter_resample.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Resampling</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Rotations of a mesh about its axes. In this model, the x axis is from the left to right; the y ...">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_rotate_thumb.png
    :alt: Rotations

  :ref:`sphx_glr_examples_01-filter_rotate.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Rotations</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Perlin noise is atype of gradient noise often used by visual effects artists to increase the ap...">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_sampling_functions_2d_thumb.png
    :alt: Sample Function: Perlin Noise in 2D

  :ref:`sphx_glr_examples_01-filter_sampling_functions_2d.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Sample Function: Perlin Noise in 2D</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Video games like Minecraft use Perlin noise to create terrain.  Here, we create a voxelized mes...">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_sampling_functions_3d_thumb.png
    :alt: Sample Function: Perlin Noise in 3D

  :ref:`sphx_glr_examples_01-filter_sampling_functions_3d.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Sample Function: Perlin Noise in 3D</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Extract thin planar slices from a volume.">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_slicing_thumb.png
    :alt: Slicing

  :ref:`sphx_glr_examples_01-filter_slicing.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Slicing</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Integrate a vector field to generate streamlines.">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_streamlines_thumb.png
    :alt: Streamlines

  :ref:`sphx_glr_examples_01-filter_streamlines.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Streamlines</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Integrate a vector field to generate streamlines on a 2D surface.">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_streamlines_2D_thumb.png
    :alt: 2D Streamlines

  :ref:`sphx_glr_examples_01-filter_streamlines_2D.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">2D Streamlines</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Increase the number of triangles in a single, connected triangular mesh.">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_subdivide_thumb.png
    :alt: Subdivide Cells

  :ref:`sphx_glr_examples_01-filter_subdivide.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Subdivide Cells</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Smoothing rough edges of a surface mesh">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_surface-smoothing_thumb.png
    :alt: Surface Smoothing

  :ref:`sphx_glr_examples_01-filter_surface-smoothing.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Surface Smoothing</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Surface reconstruction has a dedicated filter in PyVista and is handled by pyvista.PolyDataFilt...">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_surface_reconstruction_thumb.png
    :alt: Surface Reconstruction

  :ref:`sphx_glr_examples_01-filter_surface_reconstruction.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Surface Reconstruction</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Using common filters like thresholding and clipping.">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_using-filters_thumb.png
    :alt: Using Common Filters

  :ref:`sphx_glr_examples_01-filter_using-filters.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Using Common Filters</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Create a voxel model (like legos) of a closed surface or volumetric mesh.">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_voxelize_thumb.png
    :alt: Voxelize a Surface Mesh

  :ref:`sphx_glr_examples_01-filter_voxelize.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Voxelize a Surface Mesh</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example applies the warp_by_vector filter to a sphere mesh that has 3D displacement vector...">

.. only:: html

  .. image:: /examples/01-filter/images/thumb/sphx_glr_warp-by-vector_thumb.png
    :alt: Warping by Vectors

  :ref:`sphx_glr_examples_01-filter_warp-by-vector.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Warping by Vectors</div>
    </div>


.. raw:: html

    </div>


.. toctree::
   :hidden:

   /examples/01-filter/boolean-operations
   /examples/01-filter/cell-centers
   /examples/01-filter/clipping-with-surface
   /examples/01-filter/clipping
   /examples/01-filter/collisions
   /examples/01-filter/compute-normals
   /examples/01-filter/compute-volume
   /examples/01-filter/connectivity
   /examples/01-filter/contouring
   /examples/01-filter/decimate
   /examples/01-filter/distance-between-surfaces
   /examples/01-filter/extract-cells-inside-surface
   /examples/01-filter/extract-edges
   /examples/01-filter/extract-surface
   /examples/01-filter/extrude-rotate
   /examples/01-filter/extrude-trim
   /examples/01-filter/flying_edges
   /examples/01-filter/gaussian-smoothing
   /examples/01-filter/geodesic
   /examples/01-filter/glyphs
   /examples/01-filter/glyphs_table
   /examples/01-filter/gradients
   /examples/01-filter/image-fft-perlin-noise
   /examples/01-filter/image-fft
   /examples/01-filter/integrate-data
   /examples/01-filter/interpolate
   /examples/01-filter/mesh-quality
   /examples/01-filter/poly-ray-trace
   /examples/01-filter/project-plane
   /examples/01-filter/reflect
   /examples/01-filter/resample
   /examples/01-filter/rotate
   /examples/01-filter/sampling_functions_2d
   /examples/01-filter/sampling_functions_3d
   /examples/01-filter/slicing
   /examples/01-filter/streamlines
   /examples/01-filter/streamlines_2D
   /examples/01-filter/subdivide
   /examples/01-filter/surface-smoothing
   /examples/01-filter/surface_reconstruction
   /examples/01-filter/using-filters
   /examples/01-filter/voxelize
   /examples/01-filter/warp-by-vector

