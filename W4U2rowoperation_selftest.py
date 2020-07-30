#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 13:49:37 2020

@author: zino
"""

 import numpy as np
 import numpy.random as rn
 
'''
解 二元一次聯立方程式
3x + 2y = 18
-3x + y = -9

目標讓矩陣前4項變成
[1,0]
[0,1]
'''
#原始方程式
t = np.asarray([[3,2, 18],[-3, 1 ,-9]])
t

g = np.asarray([[1,-2],[0,1]])
g

# 第二列 * -2 與第一列相加
n1 = g @ t
n1

g = np.asarray([[1/9,0],[0,1]])

# 第一列 /9 
n2 = g @ n1
n2

g = np.asarray([[1,0],[3,1]])
g

# 第一列 乘3 與第二列相加
n3 = g @ n2
n3

print(n3)
print('x=',n3[0,2])
print('y=',n3[1,2])



