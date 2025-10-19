import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import griddata


n=400
X=np.linspace(-5,5,n)
Y=np.linspace(-5,5,n)
#Z=np.random.normal(0,1,(n,n)) 
def f(x,y):
    return np.sin(np.sqrt(x**2+y**2))
X1,Y1=np.meshgrid(X,Y)#生成网格坐标矩阵
Z=f(*np.meshgrid(X,Y))#把Z和X,Y绑定成网格,使Z的每个值对应X,Y的每个值

fig1=plt.figure()

plt.contourf(X,Y,Z,8,alpha=0.5,cmap=plt.cm.hot)#contourfill等高线填充/or cold
L=plt.contour(X,Y,Z,8,colors='k',linewidths=0.5)#画等高线
plt.clabel(L,inline=True,fontsize=10)

plt.xticks()
plt.yticks()


fig2=plt.figure()
x=np.random.uniform(-5,5,n)
y=np.random.uniform(-5,5,n)
h=np.random.uniform(0,1,n)
'''D=pd.DataFrame(h,index=X,columns=Y)
def g(x,y):
    c,d=str(x),str(y)
    return D.loc[c,d]
H=g(*np.meshgrid(X,Y))'''
C=griddata((x,Y),h,(X1,Y1),method='cubic')#point,value,(xi,yi)
#method='linear'/'nearest'/'cubic'
plt.contourf(X,Y,C,8,alpha=0.5,cmap='rainbow')
L=plt.contour(X,Y,C,8,colors='k',linewidths=0.5)
plt.clabel(L,inline=True,fontsize=10)

plt.show()


