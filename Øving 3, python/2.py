# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 09:17:15 2018

@author: Bruker
"""

#Taylor series

import sympy as sp
#import math
import matplotlib.pyplot as plt
import numpy as np
# oppgave 2a
t = sp.symbols('t')
f = (sp.exp(t))
y = f.series(t,0,5)
Fapprox = y.removeO()
print 'Taylor rekkeutvikling for', f
print'Med feil:',y
print'Uten feil:',Fapprox

#oppgave 2b
x = sp.symbols('x')
F = sp.sin(x)
Func = sp.lambdify(x,F,np)    
xakse = np.linspace(0,np.pi*2,100)
plt.figure()
plt.plot(xakse,Func(xakse))
plt.axis([0,2*np.pi,-1.5,1.5])
plt.title('Taylor tilnaerming av sin(x)')
plt.xlabel('x-verdier')
plt.ylabel('y-verdier')
for n in range(4,13,2):
    Fnesten = F.series(x,0,n)
    Fnesten2 = Fnesten.removeO()
    FuncNesten = sp.lambdify(x,Fnesten2,np)
    plt.plot(xakse,FuncNesten(xakse))
plt.legend(['sin(x)','N=4','N=6','N=8','N=10','N=12']) 