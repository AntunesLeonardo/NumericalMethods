# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:01:25 2021

@author: Leonardo A. Antunes
"""

a = -6
b = 6
x = 0
e = 1e-15
E = abs(b-a)
i = 0

def valor_fx(x):
    y = x + 1
    return y

while (E > e):
    E = abs(b-a)
    x = (a+b)/2
    ax = valor_fx(a)
    bx = valor_fx(b)
    xx = valor_fx(x)
    
    if ax == 0:
        print(a, "eh zero\n")
        break
    
    if bx == 0:
        print(b, "eh zero\n")
        break
    
    if xx == 0:
        print(x, "eh zero\n")
        break

    if xx*bx < 0:
        a = x
        
    if xx*ax < 0:
        b = x