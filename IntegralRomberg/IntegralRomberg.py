"""
Algorithm for solving integration through Romberg method.
Author: AntunesLeonardo
"""
# Library import ------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# Variable Input ------------------------------------------

Lim_inf = 0.0                                         # Inferior limit of the interval
Lim_sup = 1.0                                         # Superior limit of the interval
h = 0.5
k = 5
hs = [h / 2 ** i for i in range(k)]

# Function to be solved -----------------------------------
def f(x):
    return np.exp(-x**2)

def romberg(col1):

  col1 = [item for item in col1]
  n = len(col1)

  for j in range(n - 1):
    temp_col = [0] * (n - 1 - j)
    for i in range(n - 1 - j):
      power = j + 1
      temp_col[i] = (4 ** power * col1[i + 1] - col1[i]) / (4 ** power - 1)
    col1[:n - 1 - j] = temp_col
    print(f'F_{j+2}',temp_col)
  return col1[0]

def trapezio(f,a, b, d):                            

  n = int((b - a) / h)
  soma = 0
  for k in range(1, n):
    soma += f(a + k * h)
  return (h / 2) * (f(a) + 2 * soma + f(b))



# ============================== Space for Input ==============================



col1 = [trapezio(f, Lim_inf, Lim_sup, hi) for hi in hs]
print('F_1', col1)
# ============================== Error Definition =============================
n = 3                                                   # Número de Subdivisões
xa = np.linspace(Lim_inf ,Lim_sup, n)                         # Vetor de valores plot
e = 5*10**-6                                            # Erro requerido
E_a = float(0)
# ============================== Main Loop/Output =============================
r = romberg(col1)


print('\nValor da Integral Trapezoidal:',r)
#print('\nErro Total:',E_a)
# ============================== Space for Plots ==============================
plt.plot(xa, f(xa), 'b')
plt.title('F(x) = Sen (x)')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()