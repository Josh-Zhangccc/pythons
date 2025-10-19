import numpy as np
'''A=np.array([1,1,1])
B=np.array([2,2,2])

C=np.vstack((A,B))#上下合并vertical
D=np.hstack((A,B))#左右合并horizontal
print(C,C.shape)
print(D,D.shape)
E=np.concatenate((A,B,A,B),axis=0)
print(E)

print(np.split(E,2,axis=0))
print(np.array_split(E,7,axis=0))
#vsplit/hsplit
'''

a=np.array([0,1,2,3])
b=a
a[1]=0
print(a,b)#shallow copy
b=a.copy()#deep copy
a[2]=0
print(a,b)
