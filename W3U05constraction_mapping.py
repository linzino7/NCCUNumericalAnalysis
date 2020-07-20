# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:41:59 2020

@author: ASUS
"""


import numpy as np

def g1(x):
    return (np.exp(x)-1)/2

def g2(x):
    return np.log(2*x+1)

'''
g1
'''

tol = 10**(-12)

i = 0

x0 = 1.26 # 起始點 [可以換成1, -0.5,-1,2,1.256]
x1 = g1(x0)

while abs(x1-x0)>tol:
    i += 1
    x0 = x1
    x1 = g1(x0)
    print(i,x1)
    
'''
g2
'''

tol = 10**(-12)

i = 0

x0 = 3
x1 = g2(x0)

while abs(x1-x0)>tol:
    i += 1
    x0 = x1
    x1 = g2(x0)
    print(i,x1)
    
