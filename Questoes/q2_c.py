import numpy as np

f = lambda x: 2*x**3 - 11.7*x**2 + 17.7*x - 5
df = lambda x: 6*x**2 - 23.4*x + 17.7

def newton(f, df, x0, n):
    for i in range(n):
        x0 = x0 - f(x0)/df(x0)
    return round(x0, 3)

root = newton(f, df, 3, 3)
print(root)

