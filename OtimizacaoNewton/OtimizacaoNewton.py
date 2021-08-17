"""
Created on Mon Jun 28 15:44:56 2021

@author: Leonardo A. Antunes
"""
import numpy as np
import matplotlib.pyplot as plt

# Inform input values --------------------------------------------
initialX, acceptableError = -20.0, 0.01

def f(x):
    return x**4 + 2*(x**3) + 8*(x**2) + 5*x

def f_1(x):
    return 4*(x**3) + 6*(x**2) + 16*x + 5

def f_2(x):
    return 12*(x**2) + 12*(x) + 16

def g(x):
    return x - (f_1(x) / f_2(x))

def Er(x1, x2):
    return np.abs((x2 - x1)) * 100

def newtonOptimizing(x0, acError):
    error = 100
    while error > acError:
        x1 = g(x0)
        error = Er(x0, x1)
        x0 = x1
    return x1

def graphGenerate(iPoint, fPoint, step):
    n = (fPoint - iPoint) / step
    mtrxX = np.zeros((int(n)), dtype='f')
    mtrxY = np.zeros((int(n)), dtype=(mtrxX.dtype))
    mtrxY_1 = np.zeros((int(n)), dtype=(mtrxX.dtype))
    mtrxY_2 = np.zeros((int(n)), dtype=(mtrxX.dtype))
    i = 0
    x = iPoint
    while i < int(n):
        mtrxX[i] = x 
        mtrxY[i] = f(x)
        mtrxY_1[i] = f_1(x)
        mtrxY_2[i] = f_2(x)
        i += 1
        x += step
    
    plt.plot(mtrxX, mtrxY, ls='-', lw=1.5, c='b', label="f(x)")
    plt.plot(mtrxX, mtrxY_1, ls=':', lw=1.5, c='m', label="f'(x)")
    plt.plot(mtrxX, mtrxY_2, ls='-.', lw=1.5, c='r', label="f''(x)")
    plt.grid(color = 'k', ls = ':', lw = 0.5)
    plt.legend()
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.title("Método de Newton - Plot")
    #plt.show()
    
x = newtonOptimizing(initialX, acceptableError)
graphGenerate(x-5, x+5, 0.1)
plt.plot(x, f(x), marker='o', c='b')
plt.show()
print("X para mínimo valor de f(x):", x)