import pyvista as pv
pl = pv.Plotter()
def create_mesh(value):
    res = int(value)
    sphere = pv.Sphere(phi_resolution=res, theta_resolution=res)
    pl.add_mesh(sphere, name="sphere", show_edges=True)
slider = pl.add_slider_widget(
    create_mesh,
    [5, 100],
    title="Resolution",
    title_opacity=0.5,
    title_color="red",
    fmt="%0.9f",
    title_height=0.08,
)
pl.show()
