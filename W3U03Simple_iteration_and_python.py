# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 12:10:11 2020

@author: ASUS
"""


import numpy as np

def g(x):
    return np.log(2*x+1)

tol = 10**(-14)

i = 0

x0 = 1.0
x1 = g(x0)

while abs(x1-x0)>tol:
    i += 1
    x0 = x1
    x1 = g(x0)
    print(i,x0)
