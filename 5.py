# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 13:34:44 2018

@author: Bruker
"""

#Pythion exercise 5
from __future__ import division
import numpy as np
import scipy
import scipy.linalg
import scipy.sparse
import scipy.sparse.linalg

nx = 3 #antall ukjente i raden
ny = 4 #antall ukjente i kolonnen
n = nx*ny #antall ukjente
d = np.ones(n)
b = -10*np.ones(n)

d0 = -4*d.copy() #midtre diagonal
d1_lower = d.copy()[0:-1] #kopierer listen fra og med element 0 til elementet før det siste elementet
d1_upper = d.copy()[0:-1] #samme som over
print d0
print d1_lower

d1_lower[nx-1::nx] = 0
d1_upper = d1_lower.copy()
print d1_lower
dnx_lower = d.copy()[0:-nx]
dnx_upper = dnx_lower.copy()
dnx_upper[0:3] = 2
print dnx_upper
b[1::3] = 0
b[n-1] = -40
b[n-3] = -40
b[n-2] = -30
print b

A = scipy.sparse.diags([d0, d1_upper, d1_lower, dnx_upper, dnx_lower], [0, 1, -1, nx, -nx], format='csc')
print A.toarray()
T = scipy.sparse.linalg.spsolve(A,b)
print T


