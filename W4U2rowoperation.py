#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 13:49:37 2020

@author: zino
"""

 import numpy as np
 import numpy.random as rn
 

I = np.mat(np.identity(3))

I

#A = np.mat(np.round(rn.rand(3,3)*10))

A = np.mat([[1.,9.,3.],
            [2.,5.,7.],
            [7.,5.,6.]])

'''
讓第二列*3 加到 第三列
'''
E1 = I.copy()
E1[2,:] = E1[1,:]*3 +E1[2,:]
E1

B = E1*A
# 看A B 差異
A
B

'''
讓第三列*2
'''
E2 = I.copy()
E2[2,:] = E2[2,:]*2
E2

B = E2 * A
A
B

'''
兩列對調
'''
E3 = I.copy()
E3[[0,1],:] = E3[[1,0],:]
E3

B = E3 * A
A
B


