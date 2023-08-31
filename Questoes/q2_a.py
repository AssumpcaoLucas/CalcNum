import numpy as np
import matplotlib.pylab as plt

f = lambda x: 2*x**3 - 11.7*x**2 + 17.7*x - 5

def plot_graphs(xi, xf, c):
    x = np.linspace(xi,xf,c)
    y_f = f(x)
    plt.plot(x,y_f,label='f(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()  

plot_graphs(-2.5, 7.5, 1000)