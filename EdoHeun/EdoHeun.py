"""
Algorithm for solving diferencial equations through Heun method.

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
Error = 1e-7                                          # Error

# Function to be solved -----------------------------------

def y_(t, y):
    return 4 * np.exp(0.8 * t) - 0.5 * y

# Function for solving ------------------------------------

def EdoHeun(a, b, ci, h, err):
    yn = ci
    E_a = 2*err
    y = y_a = 0

    for i in range(a,b,h):
        y = yn + y_(i, y)*h
        x = 0

        while (E_a > err):
            x += 1
            y_a = y
            y = yn + h * (y_(i, yn) + y_(i+h, y_a)) / 2

            e_a = E_a
            E_a = abs((y - y_a) / y)

            if(e_a < E_a):
                y = -1
        
    return y

# Results display =========================================

print('\nFunção y´ = 4e^(0,8t) - 0,5y')
print('\nMétodo Heun - Resultado:', round(EdoHeun(a, b, ci, h, Error), 4), '\n')