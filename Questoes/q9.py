import numpy as np
from numpy import cos, sin, pi

f = lambda x: x*cos(x)
df = lambda x: cos(x) - x*sin(x)

def biss(f, x0, xf, error):

    if f(x0)*f(xf) > 0 :
        raise Exception(
            "A função deve ter sinais opostos"
        )
    
    xm = (x0 + xf)/2

    if(np.abs(f(xm)) < error): return xm
    elif(np.sign(f(xm)) == np.sign(f(x0))): return biss(f,xm, xf, error )
    elif(np.sign(f(xm)) == np.sign(f(xf))): return biss(f, x0, xm, error)

root = biss(df, 0, pi/2, 0.0001)
print(root)

