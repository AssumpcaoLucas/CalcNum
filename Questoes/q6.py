import numpy as np
import matplotlib.pyplot as plt
from numpy import log10, sqrt

erro = 0.000005
Re = lambda x: 10**(0.1+1/(4*sqrt(x)))/sqrt(x) - k


def biss(f, x0, xf, error):

    if f(x0)*f(xf) > 0 :
        raise Exception(
            "A função deve ter sinais opostos"
        )
    
    xm = (x0 + xf)/2

    if(np.abs(f(xm)) < error): return xm
    elif(np.sign(f(xm)) == np.sign(f(x0))): return biss(f,xm, xf, error )
    elif(np.sign(f(xm)) == np.sign(f(xf))): return biss(f, x0, xm, error)


k = int(input('Insira Re: '))

while(k < 2500 or k > 1000000):
    k = int(input("Digite um numero entre 25000 e 1000000: "))

root = biss(Re, 0.01, 0.001, erro)
print(root)
