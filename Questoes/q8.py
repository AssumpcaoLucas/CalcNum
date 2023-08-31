import numpy as np
from numpy import cos, sin, pi

f = lambda x: 9/sin((125+x)*pi/180) + 7/sin((x)*pi/180)
df = lambda x: -9*cos((125+x)*pi/180)/(sin((125+x)*pi/180))**2 - 7*cos(x*pi/180)/(sin((x)*pi/180))**2

def biss(f, x0, xf, error):

    if f(x0)*f(xf) > 0 :
        raise Exception(
            "A função deve ter sinais opostos"
        )
    
    xm = (x0 + xf)/2

    if(np.abs(f(xm)) < error): return xm
    elif(np.sign(f(xm)) == np.sign(f(x0))): return biss(f,xm, xf, error )
    elif(np.sign(f(xm)) == np.sign(f(xf))): return biss(f, x0, xm, error)

root = biss(df, 0.1, 54.9, 0.0001)
print(root)
