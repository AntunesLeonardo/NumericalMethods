"""
Algorithm for solving diferencial equations through Medium Point method.

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
ci = 2                                                # Initial guess

# Function to be solved -----------------------------------

def y_(t, y):
    return 4 * np.exp(0.8 * t) - 0.5 * y

# Function for solving ------------------------------------

def EdoPontoMedio(a, b, ci, h):
    yNew = ci
    for i in range(a, b, h):
        yOld = yNew
        yWhat = yOld + y_(i, yOld) * h / 2
        yNew = yOld + y_(i+h/2, yWhat) * h
    return yWhat

# Results display =========================================

print('\nFunção y´ = 4e^(0,8t) - 0,5y')
print('\nMétodo Ponto Médio - Resultado:', round(EdoPontoMedio(a, b, ci, h), 4), '\n')