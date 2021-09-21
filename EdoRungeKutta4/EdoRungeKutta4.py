"""
Algorithm for solving diferencial equations through Runge Kutta method.

The input should be the step, the limits of the interval and the initial guess.
Author: AntunesLeonardo
"""
# Library import ------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# Variable Input ------------------------------------------

h = 1                                                 # Step
a = 0                                                 # Start point
b = 4                                                 # End point
ci = 3                                                # Initial guess

# Function to be solved -----------------------------------

def y_(t, y):
    return 4 * np.exp(0.8 * t) - 0.5 * y

# Function for solving ------------------------------------

def EdoRungeKutta4(a, b, ci, h):
    y = ci
    for i in range(a, b, h):
        yc = y
        k1 = y_(i, yc)
        k2 = y_(i + h/2, yc + k1*h/2)
        k3 = y_(i + h/2, yc + k2*h/2)
        k4 = y_(i + h, yc + k3*h)
        fi = (k1 + 2*k2 + 2*k3 + k4) / 6

        y = yc + fi * h
    return y

# Results display =========================================

print('\nFunção y´ = 4e^(0,8t) - 0,5y')
print('\nMétodo Runge Kutta - Resultado:', round(EdoRungeKutta4(a, b, ci, h), 4), '\n')