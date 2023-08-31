import numpy as np
import matplotlib.pyplot as plt

f = lambda x: x

def plot_graphs(xi, xf, c):
    x = np.linspace(xi,xf,c)
    y_f = f(x)
    plt.plot(x,y_f,label='f(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()  

plot_graphs(-5, 2, 1000)