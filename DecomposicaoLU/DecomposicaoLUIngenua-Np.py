"""
Solução de Sistema de Equações:

-- Decomposição LU Ingênua --


@author: Leonardo A. Antunes
"""

import numpy as np

# Matriz de Entrada ---------------------------------------------
matrizA = np.array([[0.006, 2, -16, -7], [-7, 0.01, -16, 14], [-0.02, -8, -9, 15], [2, -7, 9, 5]], dtype='f8')
# [[1, 5, 1], [2, 3, 10], [10, 2, 1]]--[[0.006, 2, -16, -7], [-7, 0.01, -16, 14], [-0.02, -8, -9, 15], [2, -7, 9, 5]]
matrizB = np.array([14, -3, 17, -12], dtype=(matrizA.dtype))
# [-8, 6, 7]--[14, -3, 17, -12]

def anulaElemeto(mtrx, lin, col, maX):
    da = mtrx[lin, col] / mtrx[col, col]
    i = 0
    while i < maX:
        mtrx[lin, i] = mtrx[lin, i] - da * mtrx[col, i]
        i += 1
    return mtrx

def triangularLU(mtrx, lins, cols):
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

def dLUIngenua(mtrxA, mtrxB):
    # Dimensões da matriz
    lins, cols = mtrxA.shape
    
    # Criação das matrizes 'd' e 'x'
    d = np.zeros((lins), dtype=(mtrxA.dtype))
    x = np.zeros((lins), dtype=(mtrxA.dtype))
    
    # Matriz A separada em 'L' e 'U'
    mtrxL, mtrxU = triangularLU(mtrxA, lins, cols)
    # print(mtrxL, '\n', mtrxU)
    
    # Cálculo dos Resultados para d
    i = 0
    while i < lins:
        Count = 0
        j = 0
        while j < i:
            Count += mtrxL[i, j] * d[j]
            j += 1
        d[i] = (mtrxB[i] - Count)
        i += 1
    
    # Cálculo dos resultados para x
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
    
print('\nDecomposição LU Ingenua:\n', dLUIngenua(matrizA, matrizB))