"""
Solução de Sistema de Equações:

-- Eliminação de Gauss Ingênua --


@author: Leonardo A. Antunes
"""

import numpy as np

# Matriz de Entrada ---------------------------------------------
matriz = np.array([[0.006, 2, -16, -7, 14], [-7, 0.01, -16, 14, -3], [-0.02, -8, -9, 15, 17], [2, -7, 9, 5, -12]], dtype='f8')
# [[0.006, 2, -16, -7, 14], [-7, 0.01, -16, 14, -3], [-0.02, -8, -9, 15, 17], [2, -7, 9, 5, -12]][[1, 5, 1, -8], [2, 3, 10, 6], [10, 2, 1, 7]]

# Funções que Modificam a Matriz
def anulaElemeto(mtrx, lin, col, maX):
    da = mtrx[lin, col] / mtrx[col, col]
    i = 0
    while i < maX + 1:
        mtrx[lin, i] = mtrx[lin, i] - da * mtrx[col, i]
        i += 1
    return mtrx

def pivotar(mtrx, lins, cols):
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

def triangular(mtrx, lins, cols):
    # O j vai antes, processo coluna-por-coluna
    j = 0
    while j < cols:
        i = 0
        while i < lins:
            if j < i:
                mtrx = anulaElemeto(mtrx, i, j, lins)
            i += 1
        j += 1
    #print(mtrx)
    return mtrx

# Função Principal
def eGaussPiv(mtrx):
    # Definição de Variáveis
    lins, cols = mtrx.shape
    # cols = lins + 1
    
    # Preenchimento da Lista de Respostas (x)
    x = np.zeros((lins), dtype=(mtrx.dtype))
    
    # Modificação da Matriz
    mtrx = pivotar(mtrx, lins, cols)
    mtrx = triangular(mtrx, lins, cols)
    # print(mtrx)
    
    # Cálculo dos Resultados
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

print('Eliminação de Gauss com Pivotamento:\n', 'X:', eGaussPiv(matriz))
print('\n\n', 'Solução biblioteca:\nX:', np.linalg.solve([[0.006, 2, -16, -7], [-7, 0.01, -16, 14], [-0.02, -8, -9, 15], [2, -7, 9, 5]], [14, -3, 17, -12]))