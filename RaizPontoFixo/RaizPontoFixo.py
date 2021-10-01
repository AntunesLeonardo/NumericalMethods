"""
Algorithm for finding x value where the function f(x) crosses the X axis.

The input should be an initial value (valorInicial) and the acceptable error (Erro).
The output is the value of x where f(x) = 0, and the number of iterations.
Author: AntunesLeonardo
"""
# Library import ------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# Variable Input ------------------------------------------

valorInicial = 0                                           # Initial value
Erro = 0.001                                               # Acceptable error

# Mathematical Function -----------------------------------

def f(x):
    return np.exp(-x) - x

def g(x):
    return np.exp(-x)

# Functions -----------------------------------------------

def Erelativo (x1, x2):
    return abs(((x2 - x1) / x2) * 100)

# Método Numérico
def RaizPontoFixo(f_, vI, Erro):
    Er = 100                                               # Sets initial relative error to a high number
    array = np.array([vI], dtype=float)                    # Creates array
    i = 0                                                  # iteration counter
    while Er > Erro:
        array = np.append(array, f_(array[i]))
        Er = Erelativo(array[i], array[i+1])
    
        print('AAAAAAAA', array)
        i+=1
    return array[-1], Er, i

# Results display =========================================

result, erroRelativo, iterations = RaizPontoFixo(g, valorInicial, Erro)
print("A raiz é", result, "Erro relativo:", erroRelativo)
print("Número de iterações:", iterations)

print('\nFunção: f(x) = e^-x - x')
print('\nValor inicial:', valorInicial)
print('\nRaiz em:', result, '\n')

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
