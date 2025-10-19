#matplotlib 中有两种绘图方式，一种是00（直接面向对象），一种是pyplot（面向函数）
#00可控制性高且可读性高，单但不易读
import matplotlib.pyplot as plt
import numpy as np
#简单
fig1=plt.figure()
x=np.linspace(0,1,100)
y=x**2
plt.scatter(x,y,c='k',alpha=0.5)
fig1.suptitle('ptplot')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0,1)
plt.ylim(0,1)
plt.grid()



#00
fig2,ax=plt.subplots()
fig2.suptitle('oo')

ax.scatter(x,y,c='k',alpha=0.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.grid()
plt.show()

#子图可见“plt subplot.py”文件
