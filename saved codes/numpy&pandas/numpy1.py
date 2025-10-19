import numpy as np
list1=[[1,2],
       [1,0]]#长得像矩阵的列表
list2=[[0,3],
       [2,1]]
array1=np.array(list1)#数组，其实就是矩阵
array2=np.array(list2)
print('dim:',array1.ndim)#维度
print('shape:',array1.shape,'size:',array1.size)
print(array1.dtype)

a=np.zeros((4,5))
print(a)
b=np.linspace(1,10,8).reshape((2,4))
print(b)
c=np.sin(b)
print(c)
print(c<0.5)
print(np.dot(array1,array2))
print(array1.dot(array2))
#np.sum()/min()/max()

