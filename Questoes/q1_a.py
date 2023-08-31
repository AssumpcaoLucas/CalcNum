import numpy as np
import matplotlib.pyplot as plt

f1 = lambda y: 400*(3 + y)
f2 = lambda y: 9.81*(3*y + y*y/2)**3

def plot_graphs(xi, xf, c):
    x = np.linspace(xi,xf,c)
    y_f1 = f1(x)
    y_f2 = f2(x)
    plt.plot(x,y_f1,label='f1(x)')
    plt.plot(x, y_f2, label = 'f2(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()  

plot_graphs(-5, 2, 1000)
