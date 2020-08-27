# -*- coding: utf-8 -*-
"""
Created on Tue May 15 14:31:27 2018

@author: Bruker
"""

import numpy as np
import matplotlib.pylab as plt
#from ODEschemes import euler

E = 1.
I = 1.
P = 1.
L = 1.

y0_0 = -P*L**3/(3*E*I)
y1_0 = P*L**2/(2*E*I)

N = 4

n_refine = 5
epsilon = np.zeros(n_refine)
for n in range(n_refine):

    x = np.linspace(0, L, N + 1)
    dx = x[1] - x[0]
    
    Y0 = np.zeros_like(x)
    Y1 = np.zeros_like(x)
    
    Y0[0] = y0_0
    Y1[0] = y1_0
    for i in range(N):
        f0 = Y1[i]
        f1 = -P*x[i]/(E*I)
        y0_p = Y0[i] + dx*f0
        y1_p = Y1[i] + dx*f1

        f0_p = y1_p
        f1_p = -P*x[i + 1]/(E*I)
        Y0[i + 1] = Y0[i] + dx*(f0 + f0_p)/2
        Y1[i + 1] = Y1[i] + dx*(f1 + f1_p)/2
    
    Y_analytical = P*(-x**3 + 3*L**2*x - 2*L**3)/(6*E*I)
    #epsilon[n] = max(abs(Y_analytical - Y0))
    epsilon[n] = np.sqrt(np.sum((Y0 - Y_analytical)**2)/(N + 1))
    
    N *= 2
observedOrder = np.log(epsilon[:-1]/epsilon[1:])/np.log(2)
print observedOrder
plt.plot(x, Y_analytical, 'k')
plt.plot(x, Y0, 'y--')
plt.legend(['y_analytical', 'y_numerical'])
plt.xlabel('x')
plt.ylabel('y')
plt.figure()
plt.plot(observedOrder)
plt.ylabel('Observed order')
plt.ylim([0, 4])
plt.show()
