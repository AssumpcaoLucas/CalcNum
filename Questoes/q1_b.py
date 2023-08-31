import numpy as np
import matplotlib.pyplot as plt

f3 = lambda y: 1-400*(3+y)/(9.81*(3*y+y*y/2)**3)

def biss(f, x0, xf, error):

    if f(x0)*f(xf) > 0 :
        raise Exception(
            "A função deve ter sinais opostos"
        )
    
    xm = (x0 + xf)/2

    if(np.abs(f(xm)) < error): return xm
    elif(np.sign(f(xm)) == np.sign(f(x0))): return biss(f,xm, xf, error )
    elif(np.sign(f(xm)) == np.sign(f(xf))): return biss(f, x0, xm, error)

root = biss(f3, 0.5, 2.5, 0.01)
print(root)