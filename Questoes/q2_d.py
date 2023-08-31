import numpy as np

f = lambda x: 2*x**3 - 11.7*x**2 + 17.7*x - 5

def secante(f ,x0, xf, n):
    x2 = (x0*f(xf) - xf*f(x0))/(f(xf)-f(x0))
    if (n > 0):
        return secante(f, xf, x2, n-1)
    else:
        return round(x2, 4)

root = secante(f, 3, 4, 3)
print(root)

