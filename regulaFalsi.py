
import math
import pandas as pd


def func(x):
    return (((9.81*68.1)/x)*(1-math.exp(-(x/68.1)*10)))-40


def regula_falsi(x1, x2, iterations):

    table_data = []

    for i in range(1, iterations + 1):
        xr = (x1 * func(x2) - x2 * func(x1)) / (func(x2) - func(x1))
        table_data.append([i, x1, x2, xr, func(x1), func(xr)])

        if func(x1) * func(xr) < 0:
            x2 = xr
        else:
            x1 = xr

    table = pd.DataFrame(table_data, columns=[
                         'Iteração', 'x1', 'x2', 'xr', 'f(x1)', 'f(xr)'])
    return table


resultado = regula_falsi(12, 16, 2)
print(resultado)
