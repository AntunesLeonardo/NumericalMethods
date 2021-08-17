"""
Algorithm for solving integration through Simpson 3/8 method.
Author: AntunesLeonardo
"""
# Library import ------------------------------------------

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

# Variable Input ------------------------------------------

Lim_inf = 0.0
Lim_sup = 0.8

aux = 'f'      # Defina se é por função ou por valores [f/v]
curve = np.array([0, 1, 2], dtype=float)

# Function to be solved -----------------------------------

def f(x):
    return 400*x**5-900*x**4+675*x**3-200*x**2+25*x+0.2

# Function for integrating --------------------------------

def IntegrateSimpson3_8(a, b, d, v):                            

    delta = (b - a) / d                                # Cálculo dos retangulos contidos na função (Soma de Riemann)
    x = a
    s = 0
    if(v == 'f'):                                      # Efetua Integral usando a função f(x) definida anteriormente
        for i in range(d):
            s = s + 3*(f(x)+f(x+delta))*delta/8
            x = x + delta
    else:                                              # Efetua Integral interpolando os pontos dados pelo usuário
        x_a = np.linspace(a,b,len(v))
        y_a  = interpolate.CubicSpline(x_a,v)
        for i in range(d):
            s = s + (y_a(x)+y_a(x+delta))*3*delta/8
            x = x + delta
    return s  

# Results display =========================================

n = int(1 / (5 * 10**-3))                               # Número de Subdivisões
print('\nFunção: f(x) = 400*x**5-900*x**4+675*x**3-200*x**2+25*x+0.2')
print('\nValor da Integral por Simpson 3/8:', IntegrateSimpson3_8(Lim_inf, Lim_sup, n, aux))
print('\nNúmero de retangulos usados:',n, '\n')

# Curve plot ==============================================

xPlot = np.linspace(Lim_inf, Lim_sup, (Lim_sup - Lim_inf) * 100)
plt.plot(xPlot, f(xPlot), lw=2, c='GoldenRod')
plt.title('Curva de f(x) no intervalo ['+str(Lim_inf)+'; '+str(Lim_sup)+']')
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()