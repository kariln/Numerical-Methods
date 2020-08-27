# -*- coding: utf-8 -*-
"""
Created on Wed May 09 18:09:39 2018

@author: Bruker
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

t_start = 0
t_slutt = 10
dt = 0.01
n = np.int(t_slutt/dt)
tvec = np.linspace(t_start,t_slutt,n+1)
Th0 = 17/36*np.pi
dTh0 = 0
d2Th0 = -9.81*np.sin(Th0)

#Eulers metode
Th_E = np.zeros(n+1)
dTh_E = Th_E.copy()
d2Th_E = Th_E.copy()

amplitude_E = []
periode_E = []

fortegn_E = 0

for i in range(n+1):
    d2Th_E[i] = d2Th0
    dTh_E[i] = dTh0
    Th_E[i] = Th0
    
    
    Th0 = Th_E[i] + dt*dTh_E[i]
    dTh0 = dTh_E[i] + dt*d2Th_E[i]
    d2Th0 = -dTh0 - 9.81*np.sin(Th0)
    
#amplitude
for i in range(n+1):
    if fortegn_E != np.sign(dTh_E[i]):
        amplitude_E.append(np.abs(Th_E[i]))
        periode_E.append(i*dt)
        fortegn_E = np.sign(dTh_E[i])
        
#periode
dp = []
N = np.size(periode_E)
xp = np.linspace(0,N,N-1)
for i in range(N-1):
    dp.append(periode_E[i+1]-periode_E[i])            
  
#Heuns metode 
Th_H = Th_E.copy()
dTh_H = Th_H.copy()
d2Th_H = Th_H.copy()

Th_pred = Th_H.copy()
dTh_pred = Th_H.copy()
d2Th_pred = Th_H.copy()

Th0_H = 17/36*np.pi
dTh0_H = 0
d2Th0_H = -9.81*np.sin(Th0_H)

amplitude_H = []
periode_H = []
fortegn_H = 0

for i in range(n+1):
    Th_pred[i] = Th0_H + dt * dTh0_H
    dTh_pred[i] = dTh0_H + dt * d2Th0_H
    d2Th_pred[i] = -dTh_pred[i] - 9.81 * np.sin(Th_pred[i])
    
    Th_H[i] = Th0_H
    dTh_H[i] = dTh0_H
    d2Th_H[i] = d2Th0_H
    
    Th0_H = Th_H[i] + 0.5*dt*(dTh_H[i] + dTh_pred[i])
    dTh0_H = dTh_H[i] + 0.5*dt*(d2Th_H[i] + d2Th_pred[i])
    d2Th0_H = -dTh0_H-9.81*np.sin(Th0_H)

for i in range(n+1):
    if fortegn_H != np.sign(dTh_H[i]):
        amplitude_H.append(np.abs(Th_H[i]))
        periode_H.append(i*dt)
        fortegn_H = np.sign(dTh_H[i])
        
        

#Plotter svingning    
plt.plot(tvec,Th_E)
plt.plot(tvec,Th_H)
plt.title('Pendel')
plt.xlabel('Tid,t [s]')
plt.ylabel('Vinkel, theta [rad]')
plt.legend(['Eulers metode','Heuns metode'], loc = 'best')
plt.show()

#Plotter amplitude
plt.plot(periode_H,amplitude_H)
plt.plot(periode_E,amplitude_E)
plt.title('Pendelens amplitude')
plt.xlabel('Tid, t [s]')
plt.ylabel('Vinkel [rad]')
plt.legend(['Heuns metode','Eulers metode'],loc='best')
plt.show()

#plotter periode
plt.plot(xp,dp)
plt.show()


