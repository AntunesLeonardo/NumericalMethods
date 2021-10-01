"""
Algorithm for finding x value where the function f(x) crosses the X axis.

The input should be the limits of the interval (a, b) and the acceptable error (e).
The output is the value of x where f(x) = 0.
Author: AntunesLeonardo
"""
# Library import ------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# Variable Input ------------------------------------------

a = -6                                                # Inferior limit
b = 6                                                 # Superior limit
e = 1e-15                                             # Acceptable error

# Mathematical Function -----------------------------------

def f(x):
    return x + 1

# Functions -----------------------------------------------

def ZeroBisseccao(f, a, b, e):
    E = abs(b - a)
    while(E > e):
        E = abs(b - a)
        x = (a + b) / 2

        if f(a) == 0:
            return a
        elif f(b) == 0:
            return b
        elif f(x) == 0:
            return x
        
        if (f(x) * f(b)) < 0:
            a = x
        elif (f(x) * f(a)) < 0:
            b = x

# Results display =========================================

result = ZeroBisseccao(f, a, b, e)
print('\nFunção: f(x) = x + 1')
print('\nIntervalo de teste:', '[', a, ', ', b, ']')
print('\nZero em:', result, '\n')

# Curve plot ==============================================

xPlot = np.linspace(a, b, (b - a) * 100)
plt.plot(xPlot, f(xPlot), lw=2, c='GoldenRod', label='f(x)')
plt.scatter(result, f(result), color='b')
plt.grid()
plt.legend()
plt.title('Função f(x)')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()