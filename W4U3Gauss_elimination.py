#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:54:45 2020

@author: zino
"""

import numpy as np
import numpy.random as rn
 
A = np.asarray([[1.,3.,-1.],
                [2.,-1.,1.],
                [0.,4.,2.]])

b = np.asarray([[8.],
                [0.],
                [-2]])

A
b


def change(M,shape,fr,to):
    '''
    列調換
    M : 矩陣
    shap: 參數的欄列數，用來創建 identity matrix
    fr : from 從那一列。
    to : 換到那一列。
    
    return : 轉換完的matrix
    '''
    I = np.identity(shape)
    I[[to,fr],:] = I[[fr,to],:]
    return I@M


def times_cut(M,shape,fr,to,times):
    '''
    乘上倍數後移除
    M : 矩陣
    shap: 參數的欄列數，用來創建 identity matrix
    fr : from 從那一列。
    to : 換到那一列。
    times : 倍數
    
    return : 轉換完的matrix
    '''
    I = np.identity(shape)
    I[to,:] = I[fr,:] * times + I[to,:]
    return I@M


def div(M,shape,fr,times):
    '''
    單純 倍數降低
    M : 矩陣
    shap: 參數的欄列數，用來創建 identity matrix
    fr : from 從那一列。
    to : 換到那一列。
    times : 倍數
    
    return : 轉換完的matrix
    '''
    I = np.identity(shape)
    I[fr,:] = I[fr,:] * 1/times 
    return I@M




As = A.shape 
nrow =  As[0]
ncol =  As[1]

M = np.append(A,b,axis=1)
M

# 左下角
for c in range(0,ncol-1):
    # 把第一列 由大到小排序 選擇排序法 
    #nrow-1-c 是因為假設只跟上一個比
    for r in range(0+c, nrow-1):
        for r2 in range(r, nrow):
            if M[r2,c] > M[r,c] :
                M = change(M,ncol,r,r+1)
                print('===sort:',M)
    
    for r in range(1+c, nrow):
        if M[r,c]!= 0:
            # 要乘上的倍數 讓下一位變成0
            times = M[r,c]/M[r-1,c] * (-1) 
            print(times)
            M = times_cut(M,ncol,r-1,r,times)
            print(M)
            

# 右上角
for c in range(ncol-1,-1,-1):
    for r in range(c,-1,-1):
        # 如果等號後方跟前方x 是倍數關西就處理
        if r == c and M[r,c+1]% M[r,c] == 0:
            times = M[r,c] 
            print(times)
            M = div(M,ncol,r,times)
            print(M)
        
        if r >0:
            print(c,r)
            # 要乘上的倍數 讓下一位變成0
            times = M[r-1,c]/M[c,c] * (-1) 
            print(times)
            M = times_cut(M,ncol,c,r-1,times)
            print(M)


#==============teacher

def Guass_elimination(A,b):
    m,n = A.shape
    R = np.mat(np.zeros([m,n+1]))
    R[:,:n] = A
    R[:,n] = b
    for i in range(m):
        maxEc = abs(R[i,i])
        maxRow = i
        for k in range(i+1,m):
            if abs(R[k,i])>maxEc:
                maxEc = R[k,i]
                maxRow = k
        R[[i,maxRow],i:] = R[[maxRow,i],i:]
        for k in range(i+1,m):
            c = -float(R[k,i])/R[i,i]
            R[k,i:] = R[k,i:]+c*R[i,i:]
            
    
    x = np.mat(np.zeros([m,1]))
    
    for i in range(m-1,-1,-1):
        x[i] = float(R[i,-1])/R[i,i]
        print(x)
        for k in range(i-1,-1,-1):
            R[k,-1] -= R[k,i]*x[i] 
            print(R)
    return x

# 方程式
A = np.mat(np.round(rn.rand(4,4)*10))
A

# 解答
xt = np.mat(np.round(rn.rand(4,1)*10))
xt

b = A*xt
b

x = Guass_elimination(A,b)
x
