import numpy as np

def newRaph(f, df, x0, error):
    if abs(f(x0)) < error:
        return x0
    return newRaph(f, df, x0 - f(x0)/df(x0), error)

def newton(f, df, x0, n):
    for i in range(n):
        x0 = x0 - f(x0)/df(x0)
        
    return round(x0, 4)