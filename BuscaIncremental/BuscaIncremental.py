# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:18:10 2021

@author: Leonardo A. Antunes
"""

a = -6
b = 6
c = 0.5

def funcao(x):
    y = x**3-9*x+3
    return y

while a < b:
    
    print("a =", a, "   x =", a+c)
    
    if funcao(a)*funcao(a+c) < 0:
        print("Há um zero entre", a, 
              "e ", a+c, "\n")
    a +=c
