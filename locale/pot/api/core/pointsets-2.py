# Camera position.
# it's hard-coded in this example
cpos = [(11.9151, 6.1139, 3.61249),
        (0.0, 0.375, 2.0),
        (-0.4254, 0.9024, -0.0678)]

grid.plot(scalars=d[:, 1], scalar_bar_args={'title': 'Y Displacement'}, cpos=cpos)