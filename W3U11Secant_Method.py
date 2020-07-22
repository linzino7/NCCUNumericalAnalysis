# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 10:44:54 2020

@author: ASUS
"""

import numpy as np

def f(x):
    '''
    連續函數
    '''
    return np.exp(x)-2*x-1

def df(x):
    '''
    連續函數微分
    '''
    return np.exp(x)-2

def secant(x0,x1):
    '''

    '''
    return x1 - f(x1) * (x1-x0)/(f(x1)-f(x0))

# 起始值
x0 = -2   #x0
x1 = -2.1
tel = 10 ** (-16)  #逼近目標 容忍值
i=0      #計算圈數

while abs(f(x0))> tel:
    tmp = secant(x0,x1)
    x0 = x1
    x1 = tmp
    i+=1

print('跑了幾圈',i)
print('x0 = ',x0)
print('f(x0) = ',f(x0))
print('format f(x0) = ',format(f(x0), '.30f'))