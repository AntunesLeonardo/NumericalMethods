"""
Created on Mon Jun 28 20:24:09 2021

@author: Leonardo A. Antunes
"""

from scipy.optimize import minimize
import numpy as np

inputValue = np.array([1, 0], dtype='f')

def f(x):
    return x[0]**4 + 2*(x[0]**3) + 8*(x[0]**2) + 5*x[0]

print("\nMétodo Nelder-Mead: ")
print(minimize(f, inputValue, method='Nelder-Mead'))

print("\nMétodo CG: ")
print(minimize(f, inputValue, method='CG'))

print("\nMétodo SLSQP: ")
print(minimize(f, inputValue, method='SLSQP'))