import numpy as np
import matplotlib.pyplot as plt

k1 = 50000
k2 = 40
m = 90
g = 9.81
h = 0.45

f = lambda y: 2*k2*y**(5/2)/5+0.5*k1*y**2 - m*g*y - m*g*h
df = lambda y: 5*k2*y**(3/2)/5 + k1*y - m*g

def newRaph(f, df, x0, error):
    if abs(f(x0)) < error:
        return x0
    return newRaph(f, df, x0 - f(x0)/df(x0), error)

root = newRaph(f, df, 1, 0.0001)
print(root)