import numpy as np

def falPos(f, x0, xf, error):

    if(np.sign(f(x0)) == np.sign(f(xf))):
        raise Exception(
            "A função deve ter sinais opostos"
        )
    
    xm = ((x0*np.abs(f(x0)) + x0*np.abs(f(xf)))/(np.abs(f(x0)) + np.abs(f(xf))))

    if(xm < error): return xm
    elif(np.sign(f(xm)) == np.sign(f(x0))): return falPos(f, xm, x0, error)
    elif(np.sign(f(xm)) == np.sign(f(xf))): return falPos(f, x0, xm, error)