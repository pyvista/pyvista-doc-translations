"""Jupyter notebook plotting module."""

import os
from .. import rcParams
from .itkplotter import PlotterITK

ALLOWED_BACKENDS = ['ipyvtk_simple', 'panel', 'ipygany', 'static', 'none']


def check_backend_env_var():
    """Set ipyvtk_vtk rcParam flag for interactive notebook rendering."""
    if 'PYVISTA_JUPYTER_BACKEND' in os.environ:
        set_jupyter_backend(os.environ['PYVISTA_JUPYTER_BACKEND'])


def set_jupyter_backend(backend):
    """Set the plotting backend for a jupyter notebook.

    Parameters
    ----------
    backend : str
        Jupyter backend to use when plotting.  Must be one of the following:

        * ``'ipyvtk_simple'`` : Render remotely and stream the
          resulting VTK images back to the client.  Supports all VTK
          methods, but suffers from lag due to remote rendering.
          Requires that a virtual framebuffer be setup when displaying
          on a headless server.  Must have ``ipyvtk_simple`` installed.

        * ``'panel'`` : Convert the VTK render window to a vtkjs
          object and then visualize that within jupyterlab. Supports
          most VTK objects.  Requires that a virtual framebuffer be
          setup when displaying on a headless server.  Must have
          ``panel`` installed.

        * ``'ipygany'`` : Convert all the meshes into ``ipygany``
          meshes and streams those to be rendered on the client side.
          Supports VTK meshes, but few others.  Aside from ``none``,
          this is the only method that does not require a virtual
          framebuffer.  Must have ``ipygany`` installed.

        * ``'static'`` : Display a single static image within the
          Jupyterlab environment.  Still requires that a virtual
          framebuffer be setup when displaying on a headless server,
          but does not require any additional modules to be installed.

        * ``'none'`` : Do not display any plots within jupyterlab,
          instead display using dedicated VTK render windows.  This
          will generate nothing on headless servers even with a
          virtual framebuffer.

    Examples
    --------
    Enable the ipygany backend.

    >>> import pyvista as pv
    >>> pv.set_jupyter_backend('ipygany')

    Enable the panel backend.

    >>> pv.set_jupyter_backend('panel')

    Enable the ipyvtk_simple backend.

    >>> pv.set_jupyter_backend('ipyvtk_simple')

    Just show static images.

    >>> pv.set_jupyter_backend('static')

    Disable all plotting within JupyterLab and display using a
    standard desktop VTK render window.

    >>> pv.set_jupyter_backend(None)  # or 'none'

    """
    # Must be a string
    if backend is None:
        backend = 'none'
    backend = backend.lower()

    try:
        import IPython
    except ImportError:  # pragma: no cover
        raise ImportError('Install IPython to display with pyvista in a notebook.')

    if backend not in ALLOWED_BACKENDS:
        backend_list_str = ', '.join([f'"{item}"' for item in ALLOWED_BACKENDS])
        raise ValueError(f'Invalid Jupyter notebook plotting backend "{backend}".\n'
                         f'Use one of the following:\n{backend_list_str}')

    # verify required packages are installed
    if backend == 'ipyvtk_simple':
        try:
            import ipyvtk_simple
        except ImportError:    # pragma: no cover
            raise ImportError('Please install `ipyvtk-simple` to use this feature')

    if backend == 'panel':
        try:
            import panel
        except ImportError:  # pragma: no cover
            raise ImportError('Please install `panel` to use this feature')
        panel.extension('vtk')

    if backend == 'ipygany':
        # raises an import error when fail
        import pyvista.jupyter.pv_ipygany

    if backend == 'none':
        backend = None

    rcParams['jupyter_backend'] = backend


# this will run on __init__ to set the backend
check_backend_env_var()
