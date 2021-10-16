import pyvista
light = pyvista.Light()
light.set_camera_light()
light.light_type
# Expected:
## <LightType.CAMERA_LIGHT: 2>
