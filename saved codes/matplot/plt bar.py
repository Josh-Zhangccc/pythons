import matplotlib.pyplot as plt
import numpy as np

n=12
X=np.arange(n)
Y1=(1-X/float(n)) * np.random.uniform(0.5,1.0,n)#随机数
Y2=(1-X/float(n)) * np.random.uniform(0.5,1.0,n)#flloat(n)表示把n转化为浮点数
plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white')
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')
for x,y in zip(X,Y1):
    plt.text(x+0,y+0.05,'%.2f'%y,ha='center',va='bottom')#'%.2f'表示保留两位小数
for x,y in zip(X,Y2):
    plt.text(x+0,-y-0.05,'-%.2f'%y,ha='center',va='top')
plt.xlim(-1,n)
plt.ylim(-1.25,1.25)
plt.xticks(())
plt.yticks(())
plt.title('Bar chart')
plt.show()
