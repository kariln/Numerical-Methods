# -*- coding: utf-8 -*-
"""
Created on Tue May 15 10:19:21 2018

@author: Bruker
"""

from __future__ import division
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols("x")
f = sp.sin(x)
f_lam = sp.lambdify(x,f,np)
xvec = np.linspace(0,2*np.pi,101)


plt.figure()

navn = ['N=4','N=6','N=8','N=10','N=12']
for i in range(4,13,2):
    Tf = f.series(x,0,i).removeO()
    print Tf
    lam_Tf = sp.lambdify(x,Tf,np)
    fvec = lam_Tf(xvec)
    plt.plot(xvec,fvec
plt.plot(xvec,f_lam(xvec),'k--')    
plt.xlim(0,2*np.pi)
plt.ylim(-1.5,1.5)
plt.title('Taylor rekkeutvikling av sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(navn,loc='best')
plt.grid()
plt.show()
    
        
