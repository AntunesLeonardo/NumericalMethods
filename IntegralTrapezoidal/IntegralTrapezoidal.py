"""
Algorithm for solving integration through Trapezoidal method.
Author: AntunesLeonardo
"""
# Library import ------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# Variable Input ------------------------------------------

Lim_inf = -1
Lim_sup = 1

# Function to be solved -----------------------------------

def f(x):
    return x + 1
    #return np.sin(x)
    #return 400*x**5-900*x**4+675*x**3-200*x**2+25*x+0.2

# Function for integrating --------------------------------

def IntegrateTrapezio(a, b, d):                            

    delta = (b - a) / d
    x = a
    s = 0
    for i in range(d):
        s += (f(x) + f(x+delta)) * delta / 2
        x += delta
    return s 

# Results display =========================================

n = int(1 / (5 * 10**-3))
I = IntegrateTrapezio(Lim_inf, Lim_sup, n)
E_t = -1/12*(-f(I)*(Lim_inf-Lim_sup)**3)
print('\nFunção f(x) = x + 1')
print('\nResultado Integral Trapezoidal:', I)
print('\nErro Total:',E_t, '\n')

# Curve plot ==============================================

xPlot = np.linspace(Lim_inf, Lim_sup, (Lim_sup - Lim_inf) * 100)
plt.plot(xPlot, f(xPlot), lw=2, c='GoldenRod')
plt.title('Curva de f(x) no intervalo ['+str(Lim_inf)+'; '+str(Lim_sup)+']')
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()