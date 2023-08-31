import numpy as np
import matplotlib.pyplot as plt

f = lambda y: 1-400*(3+y)/(9.81*(3*y+y*y/2)**3)

def falPos(f, x0, xf, error):

    if np.sign(f(x0)) == np.sign(f(xf)):
        raise Exception(
            "A função deve ter sinais opostos"
        )
    
    xm = ((x0*abs(f(x0)) + x0*abs(f(xf)))/(abs(f(x0)) + abs(f(xf))))

    if(np.abs(f(x0)) < error): return xm
    elif(np.sign(f(xm)) == np.sign(f(x0))): return falPos(f, xm, xf, error)
    elif(np.sign(f(xm)) == np.sign(f(xf))): return falPos(f, x0, xm, error)

root = falPos(f ,0.5, 2.5, 0.01)
print(root)