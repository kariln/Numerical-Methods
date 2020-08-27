# -*- coding: utf-8 -*-
"""
Created on Tue May 15 09:53:44 2018

@author: Bruker
"""
from __future__ import division
import sympy as sp
#import numpy as np

t = sp.symbols("t")
f = sp.exp(t)

def taylor(a,f,n):
    #a-punktet som taylor rekken går rundt
    #f - funksjon
    #n - antall ledd
    fT = []
    df = f
    lam_df = sp.lambdify(t,f)
    N=1
    for i in range(1,n+1):
        fT.append(lam_df(a)/N*(t-a)**i)
        N=N*i
        df = sp.diff(df,t)
        lam_df = sp.lambdify(t,df)
    print fT
    return fT
taylor(0,f,5)