:orphan:

.. _ref_examples:

Examples
========

Here is a gallery of several examples demonstrating what PyVista can
do!

All of these examples are live and available on MyBinder.

.. image:: https://static.mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/pyvista/pyvista-examples/master
   :alt: Launch on Binder



.. raw:: html

    <div class="sphx-glr-thumbnails">


.. raw:: html

    </div>

Mesh Creation
-------------

These examples demo how to read various file types into PyVista mesh objects,
create meshes from NumPy arrays, and how to create primitive geometric objects
like spheres, arrows, cubes, ellipsoids and more!
Once a mesh is loaded, it is ready for plotting with just a few lines
of code - explore these examples to get started with using PyVista for your
data.



.. raw:: html

    <div class="sphx-glr-thumbnails">


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Create an explicit structured grid from NumPy arrays.">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_create-explicit-structured-grid_thumb.png
    :alt: Creating an Explicit Structured Grid

  :ref:`sphx_glr_examples_00-load_create-explicit-structured-grid.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Creating an Explicit Structured Grid</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The &quot;Hello, world!&quot; of VTK">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_create-geometric-objects_thumb.png
    :alt: Geometric Objects

  :ref:`sphx_glr_examples_00-load_create-geometric-objects.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Geometric Objects</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Create a Kochanek spline/polyline from a numpy array of XYZ vertices.">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_create-kochanek-spline_thumb.png
    :alt: Create a Kochanek Spline

  :ref:`sphx_glr_examples_00-load_create-kochanek-spline.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Create a Kochanek Spline</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Creating parametric objects">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_create-parametric-geometric-objects_thumb.png
    :alt: Parametric Geometric Objects

  :ref:`sphx_glr_examples_00-load_create-parametric-geometric-objects.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Parametric Geometric Objects</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Here we use pyvista.Box to make `pixel art &lt;https://en.wikipedia.org/wiki/Pixel_art&gt;`_. Pixel s...">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_create-pixel-art_thumb.png
    :alt: Pixel Art of ALIEN MONSTERS

  :ref:`sphx_glr_examples_00-load_create-pixel-art.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Pixel Art of ALIEN MONSTERS</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="PyVista wraps the vtk.vtkPlatonicSolidSource filter as pyvista.PlatonicSolid.">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_create-platonic-solids_thumb.png
    :alt: Platonic Solids

  :ref:`sphx_glr_examples_00-load_create-platonic-solids.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Platonic Solids</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Create a pyvista.PolyData object from a point cloud of vertices and scalar arrays for those poi...">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_create-point-cloud_thumb.png
    :alt: Create Point Cloud

  :ref:`sphx_glr_examples_00-load_create-point-cloud.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Create Point Cloud</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="A pyvista.PointSet is a concrete class representing a set of points that specifies the interfac...">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_create-pointset_thumb.png
    :alt: Create a PointSet

  :ref:`sphx_glr_examples_00-load_create-pointset.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Create a PointSet</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Creating a pyvista.PolyData (surface mesh) from vertices and faces.">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_create-poly_thumb.png
    :alt: Create PolyData

  :ref:`sphx_glr_examples_00-load_create-poly.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Create PolyData</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example shows how to build a simple pyvista.PolyData using triangle strips.">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_create-polydata-strips_thumb.png
    :alt: Triangle Strips

  :ref:`sphx_glr_examples_00-load_create-polydata-strips.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Triangle Strips</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example shows how to build a simple pyvista.UnstructuredGrid using polyhedra. We will be u...">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_create-polyhedron_thumb.png
    :alt: Unstructured Grid with Polyhedra

  :ref:`sphx_glr_examples_00-load_create-polyhedron.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Unstructured Grid with Polyhedra</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Create a spline/polyline from a numpy array of XYZ vertices using pyvista.Spline.">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_create-spline_thumb.png
    :alt: Creating a Spline

  :ref:`sphx_glr_examples_00-load_create-spline.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Creating a Spline</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Create a StructuredGrid surface from NumPy arrays">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_create-structured-surface_thumb.png
    :alt: Creating a Structured Surface

  :ref:`sphx_glr_examples_00-load_create-structured-surface.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Creating a Structured Surface</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Drape a surface (2D array) from a line in 3D space.">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_create-surface-draped_thumb.png
    :alt: Drape 2D Surface From Line

  :ref:`sphx_glr_examples_00-load_create-surface-draped.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Drape 2D Surface From Line</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Create a surface from a set of points through a Delaunay triangulation.">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_create-tri-surface_thumb.png
    :alt: Create Triangulated Surface

  :ref:`sphx_glr_examples_00-load_create-tri-surface.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Create Triangulated Surface</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Plot connections between points in 3D as cylinders, colored by scalars.">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_create-truss_thumb.png
    :alt: Plot Truss-like FEA Solution with Cylinders

  :ref:`sphx_glr_examples_00-load_create-truss.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Plot Truss-like FEA Solution with Cylinders</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Create a simple uniform grid from a 3D NumPy array of values.">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_create-uniform-grid_thumb.png
    :alt: Creating a Uniform Grid

  :ref:`sphx_glr_examples_00-load_create-uniform-grid.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Creating a Uniform Grid</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Create an irregular, unstructured grid from NumPy arrays.">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_create-unstructured-surface_thumb.png
    :alt: Creating an Unstructured Grid

  :ref:`sphx_glr_examples_00-load_create-unstructured-surface.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Creating an Unstructured Grid</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example extends the create_unstructured_example example by including an explanation of lin...">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_linear-cells_thumb.png
    :alt: Linear Cells

  :ref:`sphx_glr_examples_00-load_linear-cells.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Linear Cells</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Note this feature is only available for vtk&gt;=9.">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_load-gltf_thumb.png
    :alt: Working with glTF Files

  :ref:`sphx_glr_examples_00-load_load-gltf.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Working with glTF Files</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Working with VRML Files">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_load-vrml_thumb.png
    :alt: Working with VRML Files

  :ref:`sphx_glr_examples_00-load_load-vrml.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Working with VRML Files</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="PyVista leverages `meshio`_ to read many mesh formats not natively supported by VTK including t...">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_read-dolfin_thumb.png
    :alt: Read FEniCS/Dolfin Meshes

  :ref:`sphx_glr_examples_00-load_read-dolfin.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Read FEniCS/Dolfin Meshes</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Read a dataset from a known file type.">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_read-file_thumb.png
    :alt: Load and Plot from a File

  :ref:`sphx_glr_examples_00-load_read-file.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Load and Plot from a File</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Read and plot image files (JPEG, TIFF, PNG, etc).">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_read-image_thumb.png
    :alt: Read Image Files

  :ref:`sphx_glr_examples_00-load_read-image.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Read Image Files</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The VTK library supports parallel file formats. Reading meshes broken up into several files is ...">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_read-parallel_thumb.png
    :alt: Parallel Files

  :ref:`sphx_glr_examples_00-load_read-parallel.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Parallel Files</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Load data using a Reader">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_reader_thumb.png
    :alt: Load data using a Reader

  :ref:`sphx_glr_examples_00-load_reader.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Load data using a Reader</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Use a topographic surface to create a 3D terrain-following mesh.">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_terrain-mesh_thumb.png
    :alt: Terrain Following Mesh

  :ref:`sphx_glr_examples_00-load_terrain-mesh.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Terrain Following Mesh</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="- numpy arrays - trimesh.Trimesh meshes - VTK objects">

.. only:: html

  .. image:: /examples/00-load/images/thumb/sphx_glr_wrap-trimesh_thumb.png
    :alt: Wrapping Other Objects

  :ref:`sphx_glr_examples_00-load_wrap-trimesh.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Wrapping Other Objects</div>
    </div>


.. raw:: html

    </div>

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

Plotting
--------

These examples show case many of the possibilities for altering how you display
spatial data. Explore these examples to learn how to leverage our powerful 3D
plotting routines to perform tasks like:

* Color mapping scalar values with ``matplotlib`` colormaps
* Creating animations as GIFs or movie files
* Showing the edges and nodes of different mesh types
* Use sophisticated lighting techniques like smooth shading or Eye Dome Lighting
* Glyph a vector or scalar field on a mesh (place/orient a mesh on another mesh's nodes and scale/orient based on data values)
* Label points in 3D space along side your meshes
* Creating side-by-side comparisons
* Making a dataset transparent or using a scalar value to map opacity
* Adding textures/images draped over a mesh (texture mapping)
* Rendering a depth image   



.. raw:: html

    <div class="sphx-glr-thumbnails">


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="PyVista supports three types of anti-aliasing:">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_anti-aliasing_thumb.png
    :alt: Anti-Aliasing

  :ref:`sphx_glr_examples_02-plot_anti-aliasing.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Anti-Aliasing</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="By default front and backface rendering uses the same properties. In certain situations it can ...">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_backface_props_thumb.png
    :alt: Setting Backface Properties

  :ref:`sphx_glr_examples_02-plot_backface_props.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Setting Backface Properties</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Add a background image with pyvista.Plotter.add_background_image.">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_background_image_thumb.png
    :alt: Background Image

  :ref:`sphx_glr_examples_02-plot_background_image.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Background Image</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Blurring">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_blurring_thumb.png
    :alt: Blurring

  :ref:`sphx_glr_examples_02-plot_blurring.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Blurring</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example demonstrates to show bounds within a pyvista.Plotter using pyvista.Plotter.show_gr...">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_bounds_thumb.png
    :alt: Plotting Bounds

  :ref:`sphx_glr_examples_02-plot_bounds.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Plotting Bounds</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example shows how different types of charts can be added to the scene. A more complex exam...">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_chart_basics_thumb.png
    :alt: Chart Basics

  :ref:`sphx_glr_examples_02-plot_chart_basics.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Chart Basics</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example shows how you can combine multiple charts as overlays in the same renderer. For an...">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_chart_overlays_thumb.png
    :alt: Chart Overlays

  :ref:`sphx_glr_examples_02-plot_chart_overlays.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Chart Overlays</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example demonstrates how to remove elements from a scene.">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_clear_thumb.png
    :alt: Clearing a Mesh or the Entire Plot

  :ref:`sphx_glr_examples_02-plot_clear.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Clearing a Mesh or the Entire Plot</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Use a Matplotlib, Colorcet, cmocean, or custom colormap when plotting scalar values.">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_cmap_thumb.png
    :alt: Colormap Choices

  :ref:`sphx_glr_examples_02-plot_cmap.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Colormap Choices</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Demonstrate how to pick individual blocks of a pyvista.MultiBlock using pyvista.Plotter.enable_...">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_composite-picking_thumb.png
    :alt: Composite Picking

  :ref:`sphx_glr_examples_02-plot_composite-picking.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Composite Picking</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="For this example, we will showcase the difference that depth peeling provides.">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_depth-peeling_thumb.png
    :alt: Depth Peeling

  :ref:`sphx_glr_examples_02-plot_depth-peeling.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Depth Peeling</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example shows how you can use pyvista.Plotter.enable_depth_of_field to highlight part of y...">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_depth_of_field_thumb.png
    :alt: Depth of Field Plotting

  :ref:`sphx_glr_examples_02-plot_depth_of_field.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Depth of Field Plotting</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Create a spline and generate labels along the spline based on distance along a spline.">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_distance-along-spline_thumb.png
    :alt: Label based on Distance on Line

  :ref:`sphx_glr_examples_02-plot_distance-along-spline.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Label based on Distance on Line</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Show the edges of all geometries within a mesh">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_edges_thumb.png
    :alt: Show Edges

  :ref:`sphx_glr_examples_02-plot_edges.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Show Edges</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Eye-Dome Lighting (EDL) is a non-photorealistic, image-based shading technique designed to impr...">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_edl_thumb.png
    :alt: Eye Dome Lighting

  :ref:`sphx_glr_examples_02-plot_edl.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Eye Dome Lighting</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Add a floor/wall at the boundary of the rendering scene.">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_floors_thumb.png
    :alt: Plot with Floors

  :ref:`sphx_glr_examples_02-plot_floors.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Plot with Floors</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Specify specific cells to hide when plotting.">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_ghost-cells_thumb.png
    :alt: Hide Cells with Ghosting

  :ref:`sphx_glr_examples_02-plot_ghost-cells.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Hide Cells with Ghosting</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Create a GIF Movie">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_gif_thumb.png
    :alt: Create a GIF Movie

  :ref:`sphx_glr_examples_02-plot_gif.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Create a GIF Movie</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Plot a depth image as viewed from a camera overlooking the &quot;hills&quot; example mesh.">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_image_depth_thumb.png
    :alt: Render a depth image

  :ref:`sphx_glr_examples_02-plot_image_depth.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Render a depth image</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The pyvista.Plotter.add_mesh method has an interpolate_before_map argument that affects the way...">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_interpolate-before-map_thumb.png
    :alt: Interpolate Before Mapping

  :ref:`sphx_glr_examples_02-plot_interpolate-before-map.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Interpolate Before Mapping</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Make an animation of an isovalue through a volumetric dataset">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_isovalue_thumb.png
    :alt: Moving Isovalue

  :ref:`sphx_glr_examples_02-plot_isovalue.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Moving Isovalue</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Use string arrays in a point set to label points">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_labels_thumb.png
    :alt: Label Points

  :ref:`sphx_glr_examples_02-plot_labels.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Label Points</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Control aspects of the rendered mesh&#x27;s lighting such as Ambient, Diffuse, and Specular. These o...">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_lighting_mesh_thumb.png
    :alt: Lighting Properties

  :ref:`sphx_glr_examples_02-plot_lighting_mesh.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Lighting Properties</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Linked Views in Subplots">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_linked_thumb.png
    :alt: Linked Views in Subplots

  :ref:`sphx_glr_examples_02-plot_linked.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Linked Views in Subplots</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The pyvista.LookupTable can be used to have fine-tuned control over the mapping between a pyvis...">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_lookup-table_thumb.png
    :alt: Lookup Tables

  :ref:`sphx_glr_examples_02-plot_lookup-table.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Lookup Tables</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Picking Meshes">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_mesh-picking_thumb.png
    :alt: Picking Meshes

  :ref:`sphx_glr_examples_02-plot_mesh-picking.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Picking Meshes</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Create an animated MP4 movie of a rendering scene.">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_movie_thumb.png
    :alt: Create a MP4 Movie

  :ref:`sphx_glr_examples_02-plot_movie.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Create a MP4 Movie</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Create an animated GIF by generating glyphs using pyvista.DataSet.glyph using pyvista.Sphere.">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_movie_glyphs_thumb.png
    :alt: Save a Movie Using Glyphs

  :ref:`sphx_glr_examples_02-plot_movie_glyphs.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Save a Movie Using Glyphs</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Create a GIF Movie of a Static Object with a Moving Colormap">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_moving_cmap_thumb.png
    :alt: Create a GIF Movie of a Static Object with a Moving Colormap

  :ref:`sphx_glr_examples_02-plot_moving_cmap.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Create a GIF Movie of a Static Object with a Moving Colormap</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip=" Subplotting: having multiple scenes in a single window">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_multi-window_thumb.png
    :alt: Multi-Window Plot

  :ref:`sphx_glr_examples_02-plot_multi-window.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Multi-Window Plot</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Plot a mesh&#x27;s scalar array with an opacity transfer function or opacity mapping based on a scal...">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_opacity_thumb.png
    :alt: Plot with Opacity

  :ref:`sphx_glr_examples_02-plot_opacity.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Plot with Opacity</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Orbit around a scene.">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_orbit_thumb.png
    :alt: Orbiting

  :ref:`sphx_glr_examples_02-plot_orbit.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Orbiting</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="View three orthogonal slices from a mesh.">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_ortho-slices_thumb.png
    :alt: Orthogonal Slices

  :ref:`sphx_glr_examples_02-plot_ortho-slices.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Orthogonal Slices</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="VTK 9 introduced Physically Based Rendering (PBR) and we have exposed that functionality in PyV...">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_pbr_thumb.png
    :alt: Physically Based Rendering

  :ref:`sphx_glr_examples_02-plot_pbr.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Physically Based Rendering</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Interpolate the scalars of a dataset over a circular arc.">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_plot-over-circular-arc_thumb.png
    :alt: Plot Scalars Over a Circular Arc

  :ref:`sphx_glr_examples_02-plot_plot-over-circular-arc.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Plot Scalars Over a Circular Arc</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Plot the values of a dataset over a line through that dataset">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_plot-over-line_thumb.png
    :alt: Plot Over Line

  :ref:`sphx_glr_examples_02-plot_plot-over-line.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Plot Over Line</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example demonstrates how to add point scalars for each individual cell to a dataset.">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_point-cell-scalars_thumb.png
    :alt: Point Cell Scalars

  :ref:`sphx_glr_examples_02-plot_point-cell-scalars.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Point Cell Scalars</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Plotting Point Clouds">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_point-clouds_thumb.png
    :alt: Plotting Point Clouds

  :ref:`sphx_glr_examples_02-plot_point-clouds.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Plotting Point Clouds</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Picking points on a mesh">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_point-picking_thumb.png
    :alt: Picking points on a mesh

  :ref:`sphx_glr_examples_02-plot_point-picking.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Picking points on a mesh</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Walk through of all the different capabilities of scalar bars and how a user can customize scal...">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_scalar-bars_thumb.png
    :alt: Customize Scalar Bars

  :ref:`sphx_glr_examples_02-plot_scalar-bars.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Customize Scalar Bars</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Saving Screenshots">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_screenshot_thumb.png
    :alt: Saving Screenshots

  :ref:`sphx_glr_examples_02-plot_screenshot.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Saving Screenshots</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Comparison of default, flat shading vs. smooth shading.">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_shading_thumb.png
    :alt: Types of Shading

  :ref:`sphx_glr_examples_02-plot_shading.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Types of Shading</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Extract a subset of the edges of a polygonal mesh to generate an outline (silhouette) of a mesh...">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_silhouette_thumb.png
    :alt: Silhouette Highlight

  :ref:`sphx_glr_examples_02-plot_silhouette.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Silhouette Highlight</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Generate and visualize meshes from data in longitude-latitude coordinates.">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_spherical_thumb.png
    :alt: Plot data in spherical coordinates

  :ref:`sphx_glr_examples_02-plot_spherical.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Plot data in spherical coordinates</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Demonstrate the usage of surface space ambient occlusion.">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_ssao_thumb.png
    :alt: Surface Space Ambient Occlusion

  :ref:`sphx_glr_examples_02-plot_ssao.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Surface Space Ambient Occlusion</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This allows you to pick points on the surface of a mesh.">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_surface-picking_thumb.png
    :alt: Picking a Point on the Surface of a Mesh

  :ref:`sphx_glr_examples_02-plot_surface-picking.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Picking a Point on the Surface of a Mesh</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Plot a mesh with an image projected onto it as a texture.">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_texture_thumb.png
    :alt: Applying Textures

  :ref:`sphx_glr_examples_02-plot_texture.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Applying Textures</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="PyVista allows you to set global and local plotting themes to easily set default plotting param...">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_themes_thumb.png
    :alt: Control Global and Local Plotting Themes

  :ref:`sphx_glr_examples_02-plot_themes.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Control Global and Local Plotting Themes</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This is very similar to the ref_texture_example example except it is focused on plotting aerial...">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_topo-map_thumb.png
    :alt: Topographic Map

  :ref:`sphx_glr_examples_02-plot_topo-map.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Topographic Map</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Plot a single component of a vector as a scalar array.">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_vector-component_thumb.png
    :alt: Plot Vector Component

  :ref:`sphx_glr_examples_02-plot_vector-component.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Plot Vector Component</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Volume render uniform mesh types like pyvista.UniformGrid or 3D NumPy arrays.">

.. only:: html

  .. image:: /examples/02-plot/images/thumb/sphx_glr_volume_thumb.png
    :alt: Volume Rendering

  :ref:`sphx_glr_examples_02-plot_volume.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Volume Rendering</div>
    </div>


.. raw:: html

    </div>


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

    <div class="sphx-glr-thumbcontainer" tooltip="The box widget can be enabled and disabled by the pyvista.Plotter.add_box_widget and pyvista.Pl...">

.. only:: html

  .. image:: /examples/03-widgets/images/thumb/sphx_glr_box-widget_thumb.png
    :alt: Box Widget

  :ref:`sphx_glr_examples_03-widgets_box-widget.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Box Widget</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Use a checkbox to turn on/off the visibility of meshes in a scene.">

.. only:: html

  .. image:: /examples/03-widgets/images/thumb/sphx_glr_checkbox-widget_thumb.png
    :alt: Checkbox Widget

  :ref:`sphx_glr_examples_03-widgets_checkbox-widget.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Checkbox Widget</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The line widget can be enabled and disabled by the pyvista.Plotter.add_line_widget and pyvista....">

.. only:: html

  .. image:: /examples/03-widgets/images/thumb/sphx_glr_line-widget_thumb.png
    :alt: Line Widget

  :ref:`sphx_glr_examples_03-widgets_line-widget.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Line Widget</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Use a class based callback to track multiple slider widgets for updating a single mesh.">

.. only:: html

  .. image:: /examples/03-widgets/images/thumb/sphx_glr_multi-slider-widget_thumb.png
    :alt: Multiple Slider Widgets

  :ref:`sphx_glr_examples_03-widgets_multi-slider-widget.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Multiple Slider Widgets</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The plane widget can be enabled and disabled by the pyvista.Plotter.add_plane_widget and pyvist...">

.. only:: html

  .. image:: /examples/03-widgets/images/thumb/sphx_glr_plane-widget_thumb.png
    :alt: Plane Widget

  :ref:`sphx_glr_examples_03-widgets_plane-widget.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Plane Widget</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The slider widget can be enabled and disabled by the pyvista.Plotter.add_slider_widget and pyvi...">

.. only:: html

  .. image:: /examples/03-widgets/images/thumb/sphx_glr_slider-bar-widget_thumb.png
    :alt: Slider Bar Widget

  :ref:`sphx_glr_examples_03-widgets_slider-bar-widget.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Slider Bar Widget</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The sphere widget can be enabled and disabled by the pyvista.Plotter.add_sphere_widget and pyvi...">

.. only:: html

  .. image:: /examples/03-widgets/images/thumb/sphx_glr_sphere-widget_thumb.png
    :alt: Sphere Widget

  :ref:`sphx_glr_examples_03-widgets_sphere-widget.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Sphere Widget</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip=" A spline widget can be enabled and disabled by the pyvista.Plotter.add_spline_widget and pyvis...">

.. only:: html

  .. image:: /examples/03-widgets/images/thumb/sphx_glr_spline-widget_thumb.png
    :alt: Spline Widget

  :ref:`sphx_glr_examples_03-widgets_spline-widget.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Spline Widget</div>
    </div>


.. raw:: html

    </div>


Lighting
--------

These examples demonstrate how to take fine-tuned control over lighting conditions
in a scene. Explore them to learn how to go beyond the default lighting setup to
truly bring out the best of your visualization:

* Choose between preset lighting systems for plotters
* Disable lighting on the mesh level
* Learn about the different light types
* Customize the shape of positional lights
* Use actors to visualize the beams of spotlights



.. raw:: html

    <div class="sphx-glr-thumbnails">


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Positional lights in PyVista have customizable beam shapes, see the ref_light_beam_shape_exampl...">

.. only:: html

  .. image:: /examples/04-lights/images/thumb/sphx_glr_actors_thumb.png
    :alt: Light Actors

  :ref:`sphx_glr_examples_04-lights_actors.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Light Actors</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Attenuation is the phenomenon of light&#x27;s intensity being gradually dampened as it propagates th...">

.. only:: html

  .. image:: /examples/04-lights/images/thumb/sphx_glr_attenuation_thumb.png
    :alt: Attenuation

  :ref:`sphx_glr_examples_04-lights_attenuation.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Attenuation</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The default directional lights are infinitely distant point sources, for which the only geometr...">

.. only:: html

  .. image:: /examples/04-lights/images/thumb/sphx_glr_beam_shape_thumb.png
    :alt: Beam Shape

  :ref:`sphx_glr_examples_04-lights_beam_shape.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Beam Shape</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Lights come in three types:">

.. only:: html

  .. image:: /examples/04-lights/images/thumb/sphx_glr_light_types_thumb.png
    :alt: Light Types

  :ref:`sphx_glr_examples_04-lights_light_types.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Light Types</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Disable mesh lighting.">

.. only:: html

  .. image:: /examples/04-lights/images/thumb/sphx_glr_mesh_lighting_thumb.png
    :alt: Disabling Mesh Lighting

  :ref:`sphx_glr_examples_04-lights_mesh_lighting.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Disabling Mesh Lighting</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The pyvista.Plotter class comes with three options for the default lighting system:">

.. only:: html

  .. image:: /examples/04-lights/images/thumb/sphx_glr_plotter_builtins_thumb.png
    :alt: Plotter Lighting Systems

  :ref:`sphx_glr_examples_04-lights_plotter_builtins.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Plotter Lighting Systems</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Demonstrate the usage of lights and shadows in PyVista.">

.. only:: html

  .. image:: /examples/04-lights/images/thumb/sphx_glr_shadows_thumb.png
    :alt: Shadows

  :ref:`sphx_glr_examples_04-lights_shadows.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Shadows</div>
    </div>


.. raw:: html

    </div>

Advanced
--------

Include here are few longer, more advanced examples from our users and
developers.



.. raw:: html

    <div class="sphx-glr-thumbnails">


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Each example should have a reference tag/key in the form:">

.. only:: html

  .. image:: /examples/99-advanced/images/thumb/sphx_glr_add-example_thumb.png
    :alt: Adding a New Gallery Example

  :ref:`sphx_glr_examples_99-advanced_add-example.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Adding a New Gallery Example</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Here is some velocity data from a glacier modelling simulation that is compared across nodes in...">

.. only:: html

  .. image:: /examples/99-advanced/images/thumb/sphx_glr_antarctica-compare_thumb.png
    :alt: Compare Field Across Mesh Regions

  :ref:`sphx_glr_examples_99-advanced_antarctica-compare.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Compare Field Across Mesh Regions</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="A pyvista.DataSet, such as pyvista.PolyData, can be extended by users.  For example, if the use...">

.. only:: html

  .. image:: /examples/99-advanced/images/thumb/sphx_glr_extending-pyvista_thumb.png
    :alt: Extending PyVista

  :ref:`sphx_glr_examples_99-advanced_extending-pyvista.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Extending PyVista</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Plot OpenFOAM data">

.. only:: html

  .. image:: /examples/99-advanced/images/thumb/sphx_glr_openfoam-example_thumb.png
    :alt: Plot OpenFOAM data

  :ref:`sphx_glr_examples_99-advanced_openfoam-example.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Plot OpenFOAM data</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This was originally posted to `pyvista/pyvista-support#486 &lt;https://github.com/pyvista/pyvista-...">

.. only:: html

  .. image:: /examples/99-advanced/images/thumb/sphx_glr_osmnx-example_thumb.png
    :alt: Plot Open Street Map Data

  :ref:`sphx_glr_examples_99-advanced_osmnx-example.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Plot Open Street Map Data</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Plot the solar system in PyVista.">

.. only:: html

  .. image:: /examples/99-advanced/images/thumb/sphx_glr_planets_thumb.png
    :alt: 3D Earth and Celestial Bodies

  :ref:`sphx_glr_examples_99-advanced_planets.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">3D Earth and Celestial Bodies</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example demonstrates the Moeller–Trumbore intersection algorithm using pyvista.">

.. only:: html

  .. image:: /examples/99-advanced/images/thumb/sphx_glr_ray-trace-moeller_thumb.png
    :alt: Visualize the Moeller–Trumbore Algorithm

  :ref:`sphx_glr_examples_99-advanced_ray-trace-moeller.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Visualize the Moeller–Trumbore Algorithm</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Single line segment ray tracing for PolyData objects.">

.. only:: html

  .. image:: /examples/99-advanced/images/thumb/sphx_glr_ray-trace_thumb.png
    :alt: Ray Tracing

  :ref:`sphx_glr_examples_99-advanced_ray-trace.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Ray Tracing</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="There are several videos online talking about how a sphere can be turned inside out in a contin...">

.. only:: html

  .. image:: /examples/99-advanced/images/thumb/sphx_glr_sphere_eversion_thumb.png
    :alt: Turning the sphere inside out

  :ref:`sphx_glr_examples_99-advanced_sphere_eversion.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Turning the sphere inside out</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example applies the warp_by_vector filter to a cube whose eigenmodes have been computed us...">

.. only:: html

  .. image:: /examples/99-advanced/images/thumb/sphx_glr_warp-by-vector-eigenmodes_thumb.png
    :alt: Displaying eigenmodes of vibration using ``warp_by_vector``

  :ref:`sphx_glr_examples_99-advanced_warp-by-vector-eigenmodes.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Displaying eigenmodes of vibration using ``warp_by_vector``</div>
    </div>


.. raw:: html

    </div>


.. toctree::
   :hidden:
   :includehidden:

   /examples/00-load/index.rst
   /examples/01-filter/index.rst
   /examples/02-plot/index.rst
   /examples/03-widgets/index.rst
   /examples/04-lights/index.rst
   /examples/99-advanced/index.rst



.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
