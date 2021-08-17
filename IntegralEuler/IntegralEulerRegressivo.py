"""
Algorithm for solving integration through Regressive Euler method.

Author: AntunesLeonardo
"""
# Library import ------------------------------------------

import numpy as np
import time

# Variable Input ------------------------------------------

Lim_inf = 0
Lim_sup = 5
y = 10

# Function to be solved -----------------------------------

def f(x):
    return  x**2 - 15 * x + 36

# Function for integrating --------------------------------
    
def IntegrateEulerRegr(a,b,y,d):
    R = 0
    aux = b
    if(aux > a):                           # Laço Regressivo da Integral
        R = R + y*d
        aux = aux - d
    return  R

# Results display =========================================

d = 5*10^-6    # definição dos passos

print('\nO resultado da Integral é:', IntegrateEulerRegr(Lim_inf, Lim_sup, y, d), '\n')