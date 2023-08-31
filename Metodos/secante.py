import numpy as np

def metSec(f, x0, xf, error):

    x1 = (x0*f(xf)-xf*f(x0))/(f(xf)-f(x0))

    if(np.abs(f(x1)) > np.abs(f(x1))): raise Exception(
            "A função não converge"
    )

    elif(np.abs(f(x1)) < error): return x1

    return metSec(f, x1, xf, error)

def secante(f ,x0, xf, n):
    x2 = (x0*f(xf) - xf*f(x0))/(f(xf)-f(x0))
    if (n > 0):
        return secante(xf, x2, n-1)
    else:
        return round(x2, 4)