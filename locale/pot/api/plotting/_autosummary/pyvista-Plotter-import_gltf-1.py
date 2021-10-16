import pyvista
from pyvista import examples
helmet_file = examples.gltf.download_damaged_helmet()  # doctest:+SKIP
texture = examples.hdr.download_dikhololo_night()  # doctest:+SKIP
pl = pyvista.Plotter()  # doctest:+SKIP
pl.import_gltf(helmet_file)  # doctest:+SKIP
pl.set_environment_texture(cubemap)  # doctest:+SKIP
pl.camera.zoom(1.8)  # doctest:+SKIP
pl.show()  # doctest:+SKIP
