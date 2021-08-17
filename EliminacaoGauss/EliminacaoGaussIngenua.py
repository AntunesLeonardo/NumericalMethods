"""
Solução de Sistema de Equações:

-- Eliminação de Gauss Ingênua --


@author: Leonardo A. Antunes
"""

# Matriz de Entrada ---------------------------------------------
matriz = [[10, 2, 1, 7], [1, 5, 1, -8], [2, 3, 10, 6]]

# Funções que Modificam a Matriz
def anulaElemeto(mtrx, lin, col, maX):
    da = mtrx[lin][col] / mtrx[col][col]
    i = 0
    while i < maX + 1:
        mtrx[lin][i] = mtrx[lin][i] - da * mtrx[col][i]
        i += 1
    return mtrx

def triangular(mtrx, lins, cols):
    matrix = mtrx
    i = 1
    while i < lins:
        j = 0
        while j < cols:
            if j < i:
                matrix = anulaElemeto(matrix, i, j, lins)
                
            j += 1
        i += 1
    print(mtrx)
    return mtrx

# Função Principal
def eGaussIng(mtrx, lins):
    # Definição de Variáveis
    x = []
    cols = lins + 1
    
    # Preenchimento da Lista de Respostas (x)
    i = 0
    while i < lins:
        x.append(0)
        i += 1
    
    # Modificação da Matriz
    mtrx = triangular(mtrx, lins, cols)
    
    # Cálculo dos Resultados
    i = 1
    while i < cols:
         j = 1
         Count = 0
         while j < i:
             Count += (mtrx[-i][-j-1] * x[lins - j])
             j += 1
         
         x[lins - i] = (-Count + mtrx[-i][cols-1]) / mtrx[-i][-j-1]
         i += 1
    return x

print('X:', eGaussIng(matriz, 3))