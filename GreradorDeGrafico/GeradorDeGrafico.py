"""
Algorithm for ploting grafics of function.

Leonardo A. Antunes
"""

import numpy as np
import matplotlib.pyplot as plt

# Inform inicial point, final point ---------------
initialP, finalP= 0, 5

def f(x):
    return (x**2 - 3)

def graphGenerate(f, a, b):
    xPlot = np.linspace(a, b, (b - a) * 100)
    plt.plot(xPlot, f(xPlot), lw=2, c='GoldenRod', label='f(x)')
    plt.legend()
    plt.grid()
    plt.title('Função f(x)')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

graphGenerate(f, initialP, finalP)