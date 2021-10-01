"""
Algorithm for finding x value where the function f(x) crosses the X axis.

The input should be the limits of the interval (a, b) and the result interval size (S).
The output is the intervals that contains the value of x where f(x) = 0.
Author: AntunesLeonardo
"""
# Library import ------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# Variable Input ------------------------------------------

a = -6                                                # Inferior limit
b = 6                                                 # Superior limit
S = 0.5                                               # Result interval size

# Mathematical Function -----------------------------------

def f(x):
    return x**3 - 9*x + 3

# Functions -----------------------------------------------

def RaizBuscaIncremental(f, a, b, S):
    result = np.array([], dtype=float)
    while a < b:
        if (f(a) * f(a + S)) < 0:
            result = np.append(result, [a, a+S])
        a += S
    return result

# Results display =========================================

result = RaizBuscaIncremental(f, a, b, S)
print('\nFunção: f(x) = x^3 - 9x + 3')
print('\nIntervalo de teste:', '[', a, ', ', b, ']')
print('\nZero no intervalo:')
for i in range(0, len(result), 2):
    print(result[i:i+2])
print('\n')

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
