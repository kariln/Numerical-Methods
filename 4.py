# -*- coding: utf-8 -*-
"""
Created on Tue May 15 19:05:36 2018

@author: Bruker
"""
import numpy as np


def diskretisere(x_min,x_max,N):
    xvec = np.linspace(x_min,x_max,N)
    return xvec

xmin = 0
xmax = 0.9
n = 91

xvec = diskretisere(xmin,xmax,n)

def analytisk_sol(x):
    y = 0.5*(np.log(np.abs(x-1))-np.log(np.abs(x+1)))+2
    return y
y0 = analytisk_sol(0)
yend = analytisk_sol(0.9)
print "Randbetingelsene er som følger:"
print "y0=", y0
print "yend=",yend

def deriv(x,Y):
    Yreturn = np.zeros(2)
    Yreturn[0] = Y[1]
    Yreturn[1] = -2*x*Y[1]**2
    return Yreturn

def Heun(x,Y0,Yreturn):
    Y_H = np.zeros.copy(x)
    dY_H = np.zeros.copy(Y_H)
    Y_p = np.zeros.copy(Y_H)
    dY_p = np.zeros.copy(Y_H)
    d2Y_p = np.zeros.copy(Y_H)
    
    y0 = Y0[0]
    dy0 = Y0[1]
    d2y0 = Yreturn[1]
    h = x[1] -x[0]
    
    for i in range(len(x)+1):
        Y_H[i] = y0
        dY_H[i] = dy0
        
        Y_p[i] = Y_H[i] + h*dY_H[i]
        dY_p[i] = dY_H[i] + h*d2y0
        d2Y_p[i] = -2*x[i+1]*dY_p[i]
        
        y0 = Y_H[i] + h/2*(dY_H[i]+dY_p[i])
        dy0 = dY_H[i] + h/2*(d2y0 + d2Y_p[i])
        d2y0 = -2*x[i+1]*dy0
    return Y_H

def shooting(x,itmax,s0,s1,tol):
    y_analytical = analytisk_sol(x)
    beta= y_analytical[x[-1]]
    
    Y_0 = [2,s0]
    Y = Heun(x,Y_0,Yreturn)[:,0]
    phi0 = Y[-1]-beta
    for it in range(itmax):
        Y_0 = [2,s1]
        Y = Heun(x,Y,Yreturn)[:,0]
        phi1 = Y[-1]-beta
        ds = -phi1*(s1-s0)/float(phi1-phi0)
        s0 = s1
        s1 = s1 +ds
        phi0 = phi1
        epsilon = np.max(np.abs(y_analytical-Y))
        
        if epsilon < tol:
            print "toleransen er møtt etter", i, "iterasjoner og med epsilon",epsilon
            break
    return Y
    
    
    
        
        
        
        
    
    




    