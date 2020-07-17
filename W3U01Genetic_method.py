# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:46:35 2020

@author: ASUS
"""

import numpy as np
import numpy.random as rn

def f(x):
    return np.exp(x)-2*x-2

f(3)

# Return a sample (or samples) from the "standard normal" distribution.
rn.randn()

x0 = 1+rn.randn()
print(x0)

# 誤差
tol = 10**-6
# 計算圈數
i = 0

# 目標找到一個x 讓某個function 逼近0
while abs(f(x0))>tol:
    x1 = rn.randn()
    if abs(f(x1))<abs(f(x0)):
        x0 = x1
        
print('跑了幾圈',i)
print('x0 = ',x0)
print('f(x0) = ',f(x0))
