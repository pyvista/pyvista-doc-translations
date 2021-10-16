import pyvista
from pyvista import examples
dragon = examples.download_dragon()
dragon.plot(cpos='xy')
