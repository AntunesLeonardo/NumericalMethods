"""
Algorithm for finding x value where the function f(x) crosses the X axis.

The input should be an initial Guess (valorInicial) and an acceptable error (Erro).
The output is the value of x where f(x) = 0, the reative error, and the number of iterations.
Author: AntunesLeonardo
"""
# Library import ------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# Variable Input ------------------------------------------

valorInicial = 0
Erro = 0.001

# Mathematical Function -----------------------------------

def f(x):
    return np.exp(-x) - x

def f_(x):
    return -np.exp(-x) - 1

# Functions -----------------------------------------------

def g(f, f_, x):                                           # Iterating function
    return x - (f(x) / f_(x))

def Erelativo (x1, x2):                                    # Relative error calculus
    Er = abs(((x2 - x1) / x2) * 100)
    return Er

def RaizNewtonRaphson(f, f_, g, vI, Erro):
    i = 0                                                  # Iteration counter
    Er = 100                                               # Set initial error to a high value
    arrayX = np.array([vI], dtype=float)                   # Creates array with the calculated valaues

    while Er > Erro:
        arrayX = np.append(arrayX, g(f, f_, arrayX[i]))
        Er = Erelativo(arrayX[i], arrayX[i+1])
        i+=1
    return arrayX[-1], Er, i

# Results display =========================================

result, erroRelativo, iterations = RaizNewtonRaphson(f, f_, g, valorInicial, Erro)
print('\nFunção: f(x) = e^-x - x')
print('\nValor inicial:', valorInicial)
print('\nRaiz em:', result)
print('\nCalculado com', iterations, 'iterações\n')

# Curve plot ==============================================

a, b = result-3, result+3                                  # Ploting limits
xPlot = np.linspace(a, b, (b - a) * 100)
plt.plot(xPlot, f(xPlot), lw=2, c='GoldenRod', label='f(x)')
plt.scatter(result, f(result), color='b', label='Raiz')
plt.scatter(valorInicial, f(valorInicial), color='k', label='V. Inicial')
plt.grid()
plt.legend()
plt.title('Função f(x)')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
