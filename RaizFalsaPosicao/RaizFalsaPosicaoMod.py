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

a = -5                                                     # Inferior limit
b = 5                                                      # Superior limit
e = 1e-10                                                  # Uncertanty acceptable (+- e)

# Mathematical Function -----------------------------------

def f(x):
    return x*2 - 3

# Functions -----------------------------------------------

def RaizFalsaPosicaoMod(f, a, b, e):
    i = 0
    E = float(abs(b - a))
    countA = 0
    countB = 0

    while E > e:
        i += 1
        E = float(abs(b - a))
        if countA > 1:
            f_a = f(a) / 2
        else:
            f_a = f(a)
        if countB > 1:
            f_b = f(b) / 2
        else:
            f_b = f(b)
        
        x = b - (f_b * (b - a)) / (f_b - f_a)

        if f_a == 0:
            result = a
            break
        elif f_b == 0:
            result = b
            break
        elif f(x) == 0:
            result = x
            break

        if f(x) * f_b < 0:
            a = x
            countA += 1
        else:
            b = x
            countB += 1
    return result, i

# Results display =========================================

result, iterations = RaizFalsaPosicaoMod(f, a, b, e)
print('\nFunção: f(x) = 2x - 3')
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