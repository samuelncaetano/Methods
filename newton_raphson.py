import pandas as pd
from sympy import symbols, diff

def func(x):
    return 2*x**3 - 11.7*x**2 + 17.7*x - 5

def newton_raphson(x0, iterations):
    table_data = []

    x = symbols('x')
    derivada_func = diff(func(x), x)
    
    for i in range(1, iterations + 1):
        xr = x0 - func(x0) / derivada_func.subs(x, x0)
        table_data.append([i, x0, func(x0), derivada_func.subs(x, x0), xr])
        x0 = xr
        
    table = pd.DataFrame(table_data, columns=['Iteração', 'x0', 'f(x0)', "f'(x0)", 'xr'])    
    return table

resultado = newton_raphson(3, 5)
print(resultado)
