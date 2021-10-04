"""
Algorithm for finding x value where the function f(x) crosses the X axis.

The input should be the equation system in form of matrix.
The output is the X solutions for the equations.
Author: AntunesLeonardo
"""
# Library import ------------------------------------------

import numpy as np

# Variable Input ------------------------------------------

matrizA = np.array([[0.006, 2, -16, -7], [-7, 0.01, -16, 14], [-0.02, -8, -9, 15], [2, -7, 9, 5]], dtype='f8')
# [[1, 5, 1], [2, 3, 10], [10, 2, 1]]--[[0.006, 2, -16, -7], [-7, 0.01, -16, 14], [-0.02, -8, -9, 15], [2, -7, 9, 5]]
matrizB = np.array([14, -3, 17, -12], dtype=(matrizA.dtype))
# [-8, 6, 7]--[14, -3, 17, -12]

# Functions -----------------------------------------------

def anulaElemeto(mtrx, lin, col, maX):                     # Tunr element to zero, and rearrenge the line
    da = mtrx[lin, col] / mtrx[col, col]
    i = 0
    while i < maX:
        mtrx[lin, i] = mtrx[lin, i] - da * mtrx[col, i]
        i += 1
    return mtrx

def triangularLU(mtrx, lins, cols):                        # Makes matrix triangular shaped
    mtrxL = np.zeros((lins, cols), dtype=(mtrx.dtype))
    mtrxU = mtrx
    # O j vai antes, processo coluna-por-coluna
    j = 0
    while j < cols:
        mtrxL[j, j] = 1
        i = 0
        while i < lins:
            if j < i:
                mtrxL[i, j] = mtrx[i, j] / mtrx[j, j]
                mtrxU = anulaElemeto(mtrxU, i, j, lins)
            i += 1
        j += 1
    # print(mtrxL, mtrxU)
    return mtrxL, mtrxU

def MatrizLUIngenua(mtrxA, mtrxB):                         # Main function
    lins, cols = mtrxA.shape                               # Get matrix shape
    d = np.zeros((lins), dtype=(mtrxA.dtype))              # Create D and X matrixes
    x = np.zeros((lins), dtype=(mtrxA.dtype))
    
    mtrxL, mtrxU = triangularLU(mtrxA, lins, cols)         # Get Lower and Upper matrix
    
    # Calculus for D
    i = 0
    while i < lins:
        Count = 0
        j = 0
        while j < i:
            Count += mtrxL[i, j] * d[j]
            j += 1
        d[i] = (mtrxB[i] - Count)
        i += 1
    
    # Calculus for X
    i = 1
    while i < lins + 1:
        Count = 0
        j = 1
        while j < i:
            Count += mtrxU[-i, -j] * x[-j]
            j += 1
        x[-i] = (d[-i] - Count) / mtrxU[-i, -j]
        i += 1
    return x

# Results display =========================================

result = MatrizLUIngenua(matrizA, matrizB)
print('\nMatriz de entrada:\n', matrizA)
print('\nResultados (LU Ingênua):\n')
for i in range(0, len(result)):
    print('X', i+1, '=', result[i])
print('')  