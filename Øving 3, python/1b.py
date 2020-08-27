# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 10:32:55 2018

@author: Bruker
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sp

T=np.linspace(0,2*math.pi,100)
plt.plot(T,np.sin(T),'r')
x = sp.symbols('x')
f = np.sin(x)
fFunc=sp.lambdify(x,f,np)
x0 = 0
F = None
for n in range(0,13):
    F += (x-x0)**n/math.factorial(n)*sp.substitution(f,x0)
    f=sp.diff(f(x),x)
    if n in range(4,13) and n%2 == 0:
        plt.plot(T,F(x))
plt.grid()
plt.axis([0,7,-2,2])
plt.show()        