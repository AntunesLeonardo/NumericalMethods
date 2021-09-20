"""
Algorithm for solving integration through Gauss-Legendre method.

The input should be the limits of the interval and the number os points to be used.
Author: AntunesLeonardo
"""
# Library import ------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# Variable Input ------------------------------------------

h = 1
a = 0
b = 4
ci = 2

# Function to be solved -----------------------------------

def y_(t, y):
    return 4 * np.exp(0.8 * t) - 0.5 * y

# Function for solving ------------------------------------

def EdoEuler(a, b, ci, h):
    yn = ci
    for i in range(0, b, h):
        a = yn
        yn += y_(i, a) * h
    return yn

# Results display =========================================

print('\nFunção y´ = 4e^(0,8t) - 0,5y')
print('\nMétodo Euler - Resultado:', round(EdoEuler(a, b, ci, h), 4), '\n')