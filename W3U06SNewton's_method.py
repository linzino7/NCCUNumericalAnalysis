# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 10:44:54 2020

@author: ASUS
"""

import numpy as np
import numpy.random as rn

def f(x):
    '''
    連續函數
    '''
    return np.exp(x)-2*x-2

def df(x):
    '''
    連續函數微分
    '''
    return np.exp(x)-2

# 起始值
x0 = 2   #x0
tel = 0  #逼近目標 容忍值
i=0      #計算圈數

while abs(f(x0))> tel:
    # 牛頓法公式
    x1 = x0 - (f(x0)/df(x0))
    x0 = x1
    i+=1

print('跑了幾圈',i)
print('x0 = ',x0)
print('f(x0) = ',f(x0))
print('format f(x0) = ',format(f(x0), '.25f'))