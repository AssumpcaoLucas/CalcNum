import numpy as np
import matplotlib.pyplot as plt
from numpy import pi

a = 0.9
q1 = 2*10**(-5)
q2 = q1
e0 = 8.85*10**(-12)
k = q1*q2/(4*pi*e0)

f = lambda x: k*x/(x**2+a**2)**(3/2)-1.25

'''
Usado para descobrir o intervalo de convergencia
def plot_graphs(xi, xf, c):
    x = np.linspace(xi,xf,c)
    y_f = f(x)
    plt.plot(x,y_f,label='f(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()  

plot_graphs(-5, 2, 1000)
'''


def metSec(f, x0, xf, error):

    x1 = (x0*f(xf)-xf*f(x0))/(f(xf)-f(x0))

    if(np.abs(f(x1)) > np.abs(f(x1))): raise Exception(
            "A função não converge"
    )

    elif(np.abs(f(x1)) < error): return x1

    return metSec(f, x1, xf, error)

root1 = metSec(f, 0, 0.5, 0.0001)
root2 = metSec(f, 0.5, 2, 0.0001)
print(round(root1, 4))
print(round(root2,4))


