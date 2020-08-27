# -*- coding: utf-8 -*-
"""
Created on Sun May 06 18:30:49 2018

@author: Bruker
"""
#import numpy as np
import matplotlib.pyplot as plt
#fibonacci
def fib(n):
    a,b,i = 0,1,1
    fibsum = []
    while i<=n:
        fibsum.append(a)
        a,b,i = b,(a+b),(i+1)
    print fibsum
    return fibsum
fibsumme = fib(20)
plt.plot(fibsumme) 
plt.show()    
        
        