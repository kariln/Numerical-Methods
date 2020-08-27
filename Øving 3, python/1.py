# -*- coding: utf-8 -*-
"""
Created on Fri Feb 09 15:14:10 2018

@author: Bruker
"""
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
t = sp.symbols('t')
v0 = sp.symbols('v0')
g = sp.symbols('g')
y = v0*t-sp.Rational(1,2)*g*t**2
print 'y =',y
v = sp.diff(y,t)
print 'v =',v
a = sp.diff(v,t)
print 'a =', a
y2 = sp.integrate(y,t)
print 'y2 =',y2
rotter = sp.solve(y,t)
lengde = len(rotter)
print 'y har',lengde,'losninger. De har verdiene',rotter[0],'og',rotter[1],'.'
rot1=rotter[0]
rot2=rotter[lengde-1]
func = sp.lambdify(t,y,np)
print 'Ved å sette inn rot1 =',rot1,'faar vi',func(rot1),'.'
print 'Ved å sette inn rot2 =',rot2,'faar vi',func(rot2),'.'
funcnum = sp.lambdify([t,v0,g],y,np)
funcvec = np.zeros(100)
funcroot = sp.lambdify([v0,g],rotter)
numfuncroot = funcroot(5,9.81)
tstart = numfuncroot[0]
tend = numfuncroot[lengde-1]
tid=np.linspace(tstart,tend,num=100)
for i in range(0,100):
    funcvec[i] = funcnum(tid[i],5,9.81)
plt.figure()
plt.plot(tid,funcvec)
