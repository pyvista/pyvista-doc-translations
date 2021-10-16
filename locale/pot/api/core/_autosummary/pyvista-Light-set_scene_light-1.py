import pyvista
light = pyvista.Light()
light.set_scene_light()
light.light_type
# Expected:
## <LightType.SCENE_LIGHT: 3>
