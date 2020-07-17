'''
this file is not correct
'''
import numpy as np 
import numpy.random as nr
import time 
def f(x):
	return np.exp(x)-2*x-2
	
print(f(5))
print(f(1))

a=1
b=2

tel= 10**(-10)
i=0
c= (a+b)/2

#print(i++)
while abs(f(c))>tel:
	print("a=",a)
	print("b=",b)
	print(f(a))
	print(f(b))
	i+=1
	c= (a+b)/2
    
	if f(c)*f(b)<0:
		a=c
	elif f(a)*f(c)<0:
		b=c


	#time.sleep(1)

print("i=",i)
print('ans=',a)
print('f(x)',f(a))

	
# plot
# 	
# t = []
# y = []

# for i in range(-5,5):
#     t.append(i)
#     y.append(f(i))
    

# import seaborn as sns
# sns.lineplot(t,y)

	