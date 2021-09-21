"""
Algorithm for solving diferencial equations through Euler method.

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

def EdoEuler(a, b, ci, h):
    yNew = ci
    for i in range(a, b, h):
        yOld = yNew
        yNew += y_(i, yOld) * h
    return yNew

# Results display =========================================

print('\nFunção y´ = 4e^(0,8t) - 0,5y')
print('\nMétodo Euler - Resultado:', round(EdoEuler(a, b, y_(0, ci), h), 4), '\n')