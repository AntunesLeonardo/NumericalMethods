"""
Algorithm for finding x value where the function f(x) crosses the X axis.

The input should be the limits of the interval (a, b) and the acceptable uncertanty (e).
The output is the value of x where f(x) = 0, and the number of iterations.
Author: AntunesLeonardo
"""
# Library import ------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# Variable Input ------------------------------------------

a = -7                                                     # Inferior limit
b = 0                                                      # Superior limit
e = 1e-15                                                  # Uncertanty acceptable (+- e)

# Mathematical Function -----------------------------------

def f(x):
    return 2*x + 5
    
# Functions -----------------------------------------------

def RaizFalsaPosicao(f, a, b, e):
    i = 0
    E = abs(b - a)

    while E > e:
        i += 1
        E = abs(b - a)
        x = b - (f(b) * (b - a)) / (f(b) - f(a))
        if f(a) == 0:
            result = a
            break
        elif f(b) == 0:
            result = b
            break
        elif f(x) == 0:
            result = x
            break
        
        if f(x) * f(b) < 0:
            a = x
        else:
            b = x
    return result, i

# Results display =========================================

result, iterations = RaizFalsaPosicao(f, a, b, e)
print('\nFunção: f(x) = 2x + 5')
print('\nIntervalo de teste: [', a, ', ', b, ']')
print('\nRaiz em:', result)
print('\nCalculado com', iterations, 'iterações\n')

# Curve plot ==============================================

xPlot = np.linspace(a, b, (b - a) * 100)
plt.plot(xPlot, f(xPlot), lw=2, c='GoldenRod', label='f(x)')
plt.scatter(result, f(result), color='b', label='Raiz')
plt.grid()
plt.legend()
plt.title('Função f(x)')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()