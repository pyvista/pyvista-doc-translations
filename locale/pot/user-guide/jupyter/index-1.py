# Enable the pythreejs backend.
#
import pyvista as pv
pv.set_jupyter_backend('pythreejs')  # doctest:+SKIP
#
# Enable the ipygany backend.
#
import pyvista as pv
pv.set_jupyter_backend('ipygany')  # doctest:+SKIP
#
# Enable the panel backend.
#
pv.set_jupyter_backend('panel')  # doctest:+SKIP
#
# Enable the ipyvtklink backend.
#
pv.set_jupyter_backend('ipyvtklink')  # doctest:+SKIP
#
# Just show static images.
#
pv.set_jupyter_backend('static')  # doctest:+SKIP
#
# Disable all plotting within JupyterLab and display using a
# standard desktop VTK render window.
#
pv.set_jupyter_backend(None)  # or 'none'
