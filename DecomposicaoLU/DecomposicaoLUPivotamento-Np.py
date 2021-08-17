"""
Solução de Sistema de Equações:

-- Decomposição LU com Pivotamento --


@author: Leonardo A. Antunes
"""

import numpy as np

# Matriz de Entrada ---------------------------------------------
matrizA = np.array([[3+2j, 2.3+2j, -16+2j, -17+7j], [-15-8j, 2.3+5j, -16+1j, 14-2j], [-5+13j, 8-9j, 60+3j, 7+9j], [-8+7j, -6+1j, 9+1j, 11+5j]], dtype=complex)
# [[1, 5, 1], [2, 3, 10], [10, 2, 1]]--[[0.006, 2, -16, -7], [-7, 0.01, -16, 14], [-0.02, -8, -9, 15], [2, -7, 9, 5]]--[[3+2j, 2.3+2j, -16+2j -17+7j], [-15-8j, 2.3+5j, -16+1j, 14-2j], [-5+13j, 8-9j, 60+3j, 7+9j], [-8+7j, -6+1j, 9+1j, 11+5j]]
matrizB = np.array([6+5j, -7.2+5j, 3+9.7j, 2-12.9j], dtype=(matrizA.dtype))
# [-8, 6, 7]--[14, -3, 17, -12]--[6+5j, -7.2+5j, 3+9.7j, 2-12.9j]

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

def pivotarLU(mtrxA, mtrxB, lins, cols):
    i = 0
    while i < lins:
        j = 0
        while i + j < lins:
            if np.absolute(mtrxA[i+j, i]) > np.absolute(mtrxA[i, i]):
                auxA = mtrxA[i].copy()
                auxB = mtrxB[i].copy()
                mtrxA[i] = mtrxA[i+j]
                mtrxB[i] = mtrxB[i+j]
                mtrxA[i+j] = auxA
                mtrxB[i+j] = auxB
            j += 1
        i += 1
    return mtrxA, mtrxB

def dLUPivot(mtrxA, mtrxB):
    # Dimensões da matriz
    lins, cols = mtrxA.shape
    
    # Criação das matrizes 'd' e 'x'
    d = np.zeros((lins), dtype=(mtrxA.dtype))
    x = np.zeros((lins), dtype=(mtrxA.dtype))
    
    # Matriz A separada em 'L' e 'U'
    mtrxA, mtrxB = pivotarLU(mtrxA, mtrxB, lins, cols)
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
    
print('\nDecomposição LU com Pivotamento:\n', dLUPivot(matrizA, matrizB))
print('\n\n', 'Solução biblioteca:\nX:', np.linalg.solve(matrizA, matrizB))