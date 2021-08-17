"""
Método Numérico: 

-- Método Aberto --


@author: Leonardo A. Antunes
"""

import math
import matplotlib.pyplot as plt

# Estimativa inicial -----------------------------------
valorInicial = 0
# Erro relativo aceitável ------------------------------
Erro = 0.001

# Passo de plotagem ------------------------------------
passo = 1e-3

# Função inicial
def f(x):
    f = math.exp(-x) - x
    return f

# Derivada Função inicial
def f_(x):
    fd = -math.exp(-x) - 1
    return fd

# Função de Iteração
def g(x):
    g = x - (f(x) / f_(x))
    return g

# Cálculo de erro relativo
def Erelativo (x1, x2):
    Er = abs(((x2 - x1) / x2) * 100)
    return Er

# Método Numérico
def newtonRaphson(vI):
    Er = 100
    array_x = []
    array_x.append(vI)

    iteracao = 0
    i = 0
    while Er > Erro:
        array_x.append(g(array_x[i]))
        Er = Erelativo(array_x[i], array_x[i+1])
    
        #print("x=", array_x[i], "   g(x)=", array_x[i+1], "   Er=", Er)
        i+=1
        iteracao += 1
    return array_x[-1], Er, iteracao;

# Plot:
def PlotFuncao(Xi, Xf, step):    
    plotx = []
    ploty = []
    axisX = [Xi, Xf]
    axisY = [0, 0]
    
    i = Xi
    while i <= Xf:
        plotx.append(i)
        ploty.append(f(i))
        i += step
  
    plt.plot(plotx, ploty, c='b')
    plt.plot(xEncontrado, f(xEncontrado), marker='o', c='k')
    plt.plot(axisX, axisY, ls=':', c='k')
    plt.show()

xEncontrado, erroRelativo, iteracoes = newtonRaphson(valorInicial)
PlotFuncao(xEncontrado - 2, xEncontrado + 2, passo)
print("A raiz é", xEncontrado, "Erro relativo:", erroRelativo)
print("Número de iterações:", iteracoes)