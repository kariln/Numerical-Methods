# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 17:22:44 2018

@author: Bruker
"""
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
##oppgave 3a
##eulers metode
#x = sp.symbols('x')
#y = sp.Rational(1,6)*(-x**3+3*x-2)
#yfunc = sp.lambdify(x,y,np)
#z = sp.diff(y,x)
#zfunc = sp.lambdify(x,z,np)
#dzdx = sp.diff(z,x)
#dzdxfunc = sp.lambdify(x,dzdx,np)
#print 'Tilnaerming av funksjonen y=',y,'ved Eulers metode. Steplengden er 1 og det utfores 25 iterasjoner'
#xakse = np.linspace(0,1, num=25)
#yakse = np.zeros(25)
#zakse = np.zeros(25)
#dzdxakse = np.zeros(25)
#y0 = yfunc(0)
#z0 = zfunc(0)
#dzdx0 = dzdxfunc(0)
#x0 = 0
#h = 1./25
#for n in range(0,25):
#    x = x0 + h*n
#    if n == 0:
#        yakse[n] = y0
#        zakse[n] = z0
#        dzdxakse[n] = dzdx0
#    else:
#        yakse[n] = yakse[n-1]+h*zakse[n-1]
#        zakse[n] = zakse[n-1]+h*dzdxakse[n-1]
#        dzdxakse[n] = -x
#plt.figure()
#plt.plot(xakse,yfunc(xakse))
#plt.plot(xakse,yakse)
#
##heuns metode
#y0 = yfunc(0)
#z0 = zfunc(0)
#dzdx0 = dzdxfunc(0)
#yakseH = np.zeros(25)
#zakseH = np.zeros(25)
#dzdxakseH = np.zeros(25)
#for N in range(0,25):
#    x = x0 + h*N
#    if N == 0:
#        yakseH[N] = y0
#        zakseH[N] = z0
#        dzdxakseH[N] = dzdx0
#    else:
#        dzdxakseH[N] = -x
#        zakseH[N] = zakseH[N-1]+0.5*h*(dzdxakseH[N-1]+dzdxakseH[N])
#        yakseH[N] = yakseH[N-1]+0.5*h*(zakseH[N-1]+zakseH[N])
#plt.plot(xakse,yakseH,'r--')
        
#opg. 3b
#Error
r = 2
error = np.zeros(25)
x = sp.symbols('x')
y = sp.Rational(1,6)*(-x**3+3*x-2)
yfunc = sp.lambdify(x,y,np)
xakse = np.linspace(0,1, num=25)
NN = 25 #N i error funksjon
E = np.zeros(4)
yakse = np.zeros(25)
zakse = np.zeros(25)
dzdxakse = np.zeros(25)
x0 = 0
y0 = 0
z0 = 0
dzdx0 = 0
deltay = 0
plass = 0
for dx in range(1,5):
    h = 0.25/dx
    plass += 1
    for n in range(0,25):
        x = x0 + h*n
        if n == 0:
            yakse[n] = y0
            zakse[n] = z0
            dzdxakse[n] = dzdx0
            deltay += (y(x)-yakse[n])**2
        else:
            yakse[n] = yakse[n-1]+h*zakse[n-1]
            zakse[n] = zakse[n-1]+h*dzdxakse[n-1]
            dzdxakse[n] = -x
            deltay += (y(x)-yakse[n])**2
    E[plass] = np.sqrt(1/25*deltay)