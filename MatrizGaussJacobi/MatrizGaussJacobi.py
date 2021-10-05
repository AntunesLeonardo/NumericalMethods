"""
Algorithm for finding x value where the function f(x) crosses the X axis.

The input should be the equation system in form of matrix.
The output is the X solutions for the equations.
Author: AntunesLeonardo
"""
# Library import ------------------------------------------

import numpy as np

# Variable Input ------------------------------------------

A = np.array([[10, 2, 1], [1, 5, 1], [2, 3, 10]], dtype=float)
B = np.array([7, -8, 6], dtype=A.dtype)
guess = np.array([0.7, -1.6, 0.6], dtype=A.dtype)

# Functions -----------------------------------------------

def jacobi(A,b,N=25,x=None):
    # Create an initial guess if needed                                                                                                                                                            
    if x is None:
        x = np.zeros(len(A[0]))

    # Create a vector of the diagonal elements of A                                                                                                                                                
    # and subtract them from A                                                                                                                                                                     
    D = np.diag(A)
    R = A - np.diagflat(D)

    # Iterate for N times                                                                                                                                                                          
    for i in range(N):
        x = (b - np.dot(R,x)) / D
    return x

# Results display =========================================

result = jacobi(A, B, N=25, x=guess)

print ("\nMatriz A:")
print(A)
print ("\nMatriz B:")
print(B)
print ("\nResultados para X (Gauss Jacobi):")
print(result)
print('')                                                  # Empty line