import pandas as pd
import sympy as sp


def func(x):
    return 2*x**3 - 11.7*x**2 + 17.7*x - 5


def secanteModificado(x, delta, iterations):
    table_data = []
    sym_x = sp.symbols('x')
    f = func(sym_x)

    for i in range(iterations):
        fx = f.subs(sym_x, x)
        fd = f.subs(sym_x, (x + delta))

        xr = x - ((delta * fx)/(fd - fx))

        table_data.append([i, x, delta, fx, fd, xr])

        x = xr

    table = pd.DataFrame(table_data, columns=[
                         'Iteração', 'x', 'delta', 'fx', 'fd', 'xr'])
    return table


resultado = secanteModificado(3, 0.01, 5)
print(resultado)
