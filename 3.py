# -*- coding: utf-8 -*-
"""
Created on Mon May 14 19:26:57 2018

@author: Bruker
"""

import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

v0,g,t = sp.symbols("v0,g,t")

y = v0*t-0.5*g*t**2
print "Funksjonen, y, er :", y

v = sp.diff(y,t)
print "Den deriverte av y, v, er:", v

a = sp.diff(v,t)
print "Den deriverte av v, a, er:", a

y2 = sp.integrate(y,t)
print "Den integrerte av y, y2, er:",y2

roots = sp.solve(y,t)
print "Røttene til y er:", roots

lam_y = sp.lambdify([t],y)
y_root1 = lam_y(roots[0])
y_root2 = lam_y(roots[1])
print "y(rot1)=",y_root1
print "y(rot2)=",y_root2

rot_funk = sp.lambdify([v0,g],roots)
numericroots = rot_funk(5,9.81)
lam_y = sp.lambdify([t,v0,g],y,np)
t0 = numericroots[0]
tend = numericroots[1]
t = np.linspace(t0,tend,num = 101)
Y = np.zeros_like(t)
for i, tau in enumerate(t):
    Y[i] = lam_y(tau,5,9.81)

plt.figure()
plt.plot(t,Y)
plt.show()

