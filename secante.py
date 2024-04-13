import pandas as pd
import sympy as sp


def func(x):
    return 2*x**3 - 11.7*x**2 + 17.7*x - 5


def secante(x0, x1, iterations):
    table_data = []
    x = sp.symbols('x')
    f = func(x)

    for i in range(iterations):
        fx0 = f.subs(x, x0)
        fx1 = f.subs(x, x1)

        xr = x1 - fx1 * ((x0 - x1)/(fx0 - fx1))

        table_data.append([i, x0, x1, fx0, fx1, xr])

        x0, x1 = x1, xr

    table = pd.DataFrame(table_data, columns=[
                         'Iteração', 'x_-1', 'x0', 'f(x_-1)', 'f(x0)', 'xr'])
    return table


resultado = secante(3, 4, 5)
print(resultado)
