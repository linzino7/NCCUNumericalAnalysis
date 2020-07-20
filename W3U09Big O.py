# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:14:45 2020

@author: ASUS

http://moocs.nccu.edu.tw/media/19147
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

# 起始值
x0 = -0.5   #x0
tel = 10**(-14)  #逼近目標 容忍值  ** 代表指數的意思
i=0      #計算圈數
c = list()

while abs(f(x0))> tel:
    # 牛頓法公式
    x1 = x0 - (f(x0)/df(x0))
    # 如果2次方會收斂到一個常數 ，他的收斂數度就是2次方
    c.append(abs(x1)/abs(x0)**2) 
    x0 = x1
    i+=1

print(c)

