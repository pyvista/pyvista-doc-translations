import pyvista
light = pyvista.Light()
light.set_headlight()
light.light_type
# Expected:
## <LightType.HEADLIGHT: 1>
