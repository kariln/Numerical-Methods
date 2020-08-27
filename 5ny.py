# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 13:29:02 2018

@author: Bruker
"""
import numpy as np
def FTSC_scheme(Told,r):
    T = np.zeros_like(Told)
    for i in range(1,nx) :
        T[i] = r*(Told[i+1]-2Told[i]+Told[i-1])+Told[i]
        
        