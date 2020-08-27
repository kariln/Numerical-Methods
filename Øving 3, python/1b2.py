# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 21:05:44 2018

@author: Bruker
"""

from __future__ import division
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
t = sp.symbols('t')
f = sp.exp(t)

print(f.series(t,0,5))

x = sp.symbols('x')
y = sp.sin(x)
X = np.linspace(0,np.pi*2,101)
F = None
yFunc = sp.lambdify(x,y,np)
plt.plot(X,yFunc(X))

for n in range(0,13):
    F = sp.series(y(x),x,0,n).remove0()
    if n>3 and n<13 and n%2 == 0:
        FFunc = sp.lambdify(x,F,np)
        plt.plot(X,FFunc(X))
    else:
        None
plt.show()
#error: sin object i linje 25 er ikke callable  
    