# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:19:26 2018

@author: Bruker
"""
import numpy as np
import scipy
import scipy.sparse
import scipy.sparse.linalg

def tridiagonal(N):
    #N = antall ukjente
    subDiag = np.zeros(N-1)
    mainDiag = np.zeros(N)
    superDiag = np.zeros(N-1)
    
    beta = 4.
    h = 1./(N+1)
    for i in range(1,N+1):
        if i > N-2:
            mainDiag = -beta**2*h-2*i
        else:
            subDiag[i] = i
            mainDiag = -beta**2*h-2*i
            superDiag = i+1
    
    A = scipy.sparse.diags([subDiag,mainDiag,superDiag],[-1,0,1],format = 'csc')
    print "Matrisen A:",A
    d = np.zeros(N)
    d[-1] = -N
    x_sparse = scipy.sparse.linalg.spsolve(A,d)
    return x_sparse
tridiagonal(5)