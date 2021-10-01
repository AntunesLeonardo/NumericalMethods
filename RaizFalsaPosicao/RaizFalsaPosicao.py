"""
Algorithm for finding x value where the function f(x) crosses the X axis.

The input should be the limits of the interval (a, b) and the result interval size (S).
The output is the intervals that contains the value of x where f(x) = 0.
Author: AntunesLeonardo
"""
# Library import ------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# Variable Input ------------------------------------------

a = -8                                                     # Inicio do intervalo
b = 0                                                      # Final do intervalo
e = 1e-15          # Indicador de precisão
x = 0              # A variável x é zerada
E = abs(b-a)       # E recebe o tamanho absoluto do intervalo
iteracoes = 0      # Contador de iterações é zerado

def f(x):
    return x + 5
    
# Functions -----------------------------------------------

def RaizFalsaPosicao(f, a, b, ):
    f(a)
while (E > e):
    # Incremento no contador de iterações
    iteracoes += 1
    
    # E é atualizado
    E = abs(b-a)
    
    # São calculados os valores de x, f(a), f(b), e f(x)
    y_a = f(a)
    y_b = f(b)
    
    x = b - (y_b * (b-a))/(y_b - y_a)
    y_x = f(x)
    
    # É testado se algum dos limites, a, b, ou x, é a raiz
    if y_a == 0:
        print(a, "é zero\n")
        break
    
    if y_b == 0:
        print(b, "é zero\n")
        break
    
    if y_x == 0:
        print(x, "é zero\n")
        break
    
    # Os limites do intervalo são reestabelecidos
    if y_x*y_b < 0:
        a = x 
        
    else:
        b = x
print("Número de Iterações: ", iteracoes)