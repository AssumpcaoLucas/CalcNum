import matplotlib.pyplot as plt
import numpy as np
from numpy import pi,linspace

R = 3
x_base = 2.026905728309901 
f = lambda h: 30 - pi*(h**2)*(3*R-h)/3
df = lambda h: -2*pi*R*h-pi*h**2

def newton(f, df, x0, n):
    for i in range(n):
        print(f"iteração {i}, x = {round(x0,4)} erro = {abs(1-x0/x_base):.2%}")
        x0 = x0 - f(x0)/df(x0)
        
    return round(x0, 4)

root = newton(f, df, 1, 3)
print(root)