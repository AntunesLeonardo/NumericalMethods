"""
Algorithm for solving integration through Simpson 1/3 method.
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

def IntegrateSimpson1_3(a, b, d, v):                            

    delta = (b - a) / d
    x = a
    s = 0
    if(v == 'f'):
        for i in range(d):
            s = s + (f(x)+f(x+delta))*delta/3
            x = x + delta
    else:
        x_a = np.linspace(a,b,len(v))
        y_a  = interpolate.CubicSpline(x_a,v)
        for i in range(d):
            s = s + (y_a(x)+y_a(x+delta))*delta/3
            x = x + delta

    return s  

# Results display =========================================

n = int(1 / (5 * 10**-3))
print('\nFunção: f(x) = 400*x**5-900*x**4+675*x**3-200*x**2+25*x+0.2')
print('\nResultado Integral por Simpson 1/3:', IntegrateSimpson1_3(Lim_inf, Lim_sup, n, aux), '\n')

# Curve plot ==============================================

xPlot = np.linspace(Lim_inf, Lim_sup, (Lim_sup - Lim_inf) * 100)
plt.plot(xPlot, f(xPlot), lw=2, c='GoldenRod')
plt.title('Curva de f(x) no intervalo ['+str(Lim_inf)+'; '+str(Lim_sup)+']')
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()