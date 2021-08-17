"""
Algorithm for solving integration through Regressive Euler method.

Author: AntunesLeonardo
"""
# Library import ------------------------------------------

import numpy as np
import time

# Variable Input ------------------------------------------

Lim_a = float(input('\nDigite o Limite Inferior:'))
Lim_b = float(input('Digite o Limite Superior:'))
y = float(input('Valor da função no limite:'))

# Function to be solved -----------------------------------

def f(x):
    return  x**2 - 15 * x + 36

# Function for integrating --------------------------------

def IntegrateEulerProg(a,b,y,d):
    R = 0
    aux = a 
    if (aux < b):                          # Laço Progressivo da Integral
        R = R + y*d
        aux = aux + d
    return  R

# Results display =========================================

d = 5*10^-6    # definição dos passos

print('\nO resultado da Integral é:', IntegrateEulerProg(Lim_a,Lim_b,y,d), '\n')