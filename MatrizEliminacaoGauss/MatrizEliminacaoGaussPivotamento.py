"""
Algorithm for finding x value where the function f(x) crosses the X axis.

The input should be the equation system in form of matrix.
The output is the X solutions for the equations.
Author: AntunesLeonardo
"""
# Library import ------------------------------------------

import numpy as np

# Variable Input ------------------------------------------

matriz = np.array([[0.006, 2, -16, -7, 14], [-7, 0.01, -16, 14, -3], [-0.02, -8, -9, 15, 17], [2, -7, 9, 5, -12]], dtype=float)
# [[0.006, 2, -16, -7, 14], [-7, 0.01, -16, 14, -3], [-0.02, -8, -9, 15, 17], [2, -7, 9, 5, -12]][[1, 5, 1, -8], [2, 3, 10, 6], [10, 2, 1, 7]]

# Functions -----------------------------------------------

def anulaElemeto(mtrx, lin, col, maX):                     # Tunr element to zero, and rearrenge the line
    da = mtrx[lin, col] / mtrx[col, col]
    i = 0
    while i < maX + 1:
        mtrx[lin, i] = mtrx[lin, i] - da * mtrx[col, i]
        i += 1
    return mtrx

def pivotar(mtrx, lins):                                   # Take higher value to top lines
    i = 0
    while i < lins:
        j = 0
        while i + j < lins:
            if np.abs(mtrx[i+j, i]) > np.abs(mtrx[i, i]):
                aux = mtrx[i].copy()
                mtrx[i] = mtrx[i+j]
                mtrx[i+j] = aux
            j += 1
        i += 1
    return mtrx

def triangular(mtrx, lins, cols):                          # Makes matrix triangular shaped
    # O j vai antes, processo coluna-por-coluna
    j = 0
    while j < cols:
        i = 0
        while i < lins:
            if j < i:
                mtrx = anulaElemeto(mtrx, i, j, lins)
            i += 1
        j += 1
    return mtrx

def MatrizEGaussPiv(mtrx):                                 # Main function
    lins, cols = mtrx.shape                                # Get matrix shape
    x = np.zeros((lins), dtype=(mtrx.dtype))               # Create results matrix
    
    mtrx = pivotar(mtrx, lins)                             # Modifications of the input matrix
    mtrx = triangular(mtrx, lins, cols)
    
    # Result calculus
    i = 1
    while i < cols:
         j = 1
         Count = 0
         while j < i:
             Count += (mtrx[-i, -j-1] * x[lins - j])
             j += 1
         
         x[lins - i] = (-Count + mtrx[-i, cols-1]) / mtrx[-i, -j-1]
         i += 1
    return x

# Results display =========================================

result = MatrizEGaussPiv(matriz)
print('\nMatriz de entrada:\n', matriz)
print('\nResultados (Gauss Ingênua):\n')
for i in range(0, len(result)):
    print('X', i+1, '=', result[i])
print('')                                                  # Empty line