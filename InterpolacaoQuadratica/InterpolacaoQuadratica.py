
#==============================================================================
# ===================== Interpolação Quadrática ===============================
#################################
# Busca de um máx/min pela interpolação

import numpy as np
import time
import matplotlib.pyplot as plt

# Inform input values -----------------------------------------
x0, x1, x2, e = -5, 5, 0, 10**-3

def otminter(limi,lims,x,e):
  a=1
  i=0
  while(a==1):
    fa = 2*np.sin(limi)-(limi**2)/10    
    fb = 2*np.sin(lims)-(lims**2)/10    
    fx = 2*np.sin(x)-(x**2)/10       
    num = fa*(lims**2-x**2)+fb*(x**2-limi**2)+fx*(limi**2-lims**2)
    den = 2*fa*(lims-x)+2*fb*(x-limi)+2*fx*(limi-lims) 
    xr = num/den                    
    fr = 2*np.sin(xr)-(xr**2)/10
    i+=1 
           
    if fx*fr < 0:
        lims = x 
        x=xr
        
    else :
        limi = x
        x=xr
       
    if (fa-xr)<e:
        a=0    
  return xr

def f(x):
    return x**4 + 2*(x**3) + 8*(x**2) + 5*x

def graphGenerate(iPoint, fPoint, step, xr):
    n = (fPoint - iPoint) / step
    mtrxX = np.zeros((int(n)), dtype='f')
    mtrxY = np.zeros((int(n)), dtype='f')
    i = 0
    x = iPoint
    while i < int(n):
        mtrxX[i] = x 
        mtrxY[i] = f(x)
        yi = f(xr)
        i += 1
        x += step
    
    plt.plot(mtrxX, mtrxY, ls='-', lw=1.5, c='b')
    plt.grid(color = 'k', ls = ':', lw = 0.5)
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.title("Interpolação quadratica - g(x)")
    plt.plot(xr,yi,marker='o')
    plt.show()

start= time.time_ns()
x = otminter(x0,x1,x2,e)
stop=time.time_ns()
# definitons for the plot of graphc
graphGenerate(x0, 50, 10**-3,x)  
print('\nX para mínimo valor de f(x):',x)
print('\n Tempo Necessário:',(stop-start)*10**-6,'ms')