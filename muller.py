import numpy as np
import pandas as pd


def func(x):
    return x**3 - 13*x - 12


def muller(x0, x1, x2, iterations):
    table_data = []
    for i in range(iterations):
        h1 = x1 - x0
        h2 = x2 - x1

        delta1 = (func(x1) - func(x0)) / h1
        delta2 = (func(x2) - func(x1)) / h2

        a = (delta2 - delta1) / (h2 + h1)
        b = a * h2 + delta2
        c = func(x2)

        discriminant = np.sqrt(b**2 - 4*a*c)

        if abs(b + discriminant) > abs(b - discriminant):
            den = b + discriminant
        else:
            den = b - discriminant

        dx = -2 * c / den
        xr = x2 + dx

        table_data.append([i, x0, x1, x2, xr, h1, h2,
                          delta1, delta2, a, b, c, func(xr)])

        x0, x1, x2 = x1, x2, xr

    table = pd.DataFrame(table_data, columns=[
                         'Iteração', 'x0', 'x1', 'x2', 'xr', 'h1', 'h2', 'delta1', 'delta2', 'a', 'b', 'c', 'func(xr)'])
    return table


resultado = muller(4.5, 5.5, 5, 5)
print(resultado)
