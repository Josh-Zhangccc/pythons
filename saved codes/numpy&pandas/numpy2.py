import numpy as np
A = np.arange(2,14).reshape((3,4))
e=A.mean()
print(A,e)#平均
print(A.T)#行列转换

print(np.clip(A,5,9))#小于5的变成5
