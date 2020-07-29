#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:04:07 2020

@author: zino
"""

# Python solve Ax=b

import numpy.linalg as la
import numpy.random as rn
import numpy as np


A = np.mat(rn.randn(4,4))

A

xt = np.mat(rn.randn(4,1))

xt

b = A*xt

# 解 Ax = b 答案會跟xt 一樣
x = la.solve(A,b)

# 矩陣成向量的norm
la.norm(x-xt)

A = np.round(A*10)

A

B = A**2

# 矩陣的行列式值
la.det(A)

# 製作identity matrix 
C = np.mat(np.identity(4))

D = C+A

# 矩陣的rank 
la.matrix_rank(A)

la.matrix_rank(B)

# 抽取子矩陣
E = D[0:3,0:3]
E

v = A[:,0]
v

u = A[:,2]
u

# 向量內積
z = float(u.T*v)
z
