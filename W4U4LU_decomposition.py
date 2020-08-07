# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 23:43:06 2020

@author: ASUS
http://moocs.nccu.edu.tw/media/19155
"""


import numpy as np

A = np.asarray([[1.,3.,-1.],
                [2.,-1.,1.],
                [0.,4.,2.]])

b = np.asarray([[-8.],
                [0.],
                [-2]])




nrow , ncol = A.shape

L = np.identity(ncol)
U = A.copy()
P = L.copy()


for i in range(0,ncol):
    # 下方 11行 為 對調
    MaxN = abs(U[i,i])
    Maxcol = i
    for j in range(i+1,nrow):
        #把對角線的值 跟底下每個數字比較 找到最大的 
        if U[j,i]> MaxN:
            MaxN = U[j,i]
            Maxcol = j
    U[[i,Maxcol],:]  = U[[Maxcol,i],:] # U 先換 最重點就是要換U 因為找到比對角線大的
    P[[i,Maxcol],:]  = P[[Maxcol,i],:] # 換P
    L[[i,Maxcol],:]  = L[[Maxcol,i],:] # 因為 P23 * A =  P23 * L *  P23 * U 
    L[:,[i,Maxcol]]  = L[:,[Maxcol,i]] # 因為 P23 * A = L  P23 * U
    
    #下方實作 L U 轉換成上三角與下三角
    for j in range(i+1,nrow):
        if U[j,i] != 0 :
            # 計算C 倍
            C = U[j,i]/U[i,i] 
            # U * C
            U[j,:] = U[j,:] - U[i,:] * C
            # L * -C 
            L[j,:] = L[j,:] - L[i,:] * C * (-1)

# 相等就一樣了
# P * A = L * U
print(L@U)
print(P@A)
            
            
