import matplotlib.pyplot as plt
import numpy as np

n=1024
X=np.random.normal(0,10,n)
Y=np.random.normal(0,10,n)
C=np.arctan2(Y,X)# color
plt.scatter(X,Y,s=75,c=C,alpha=0.5)
plt.xlim(-20,20)
plt.ylim(-20,20)
plt.xticks(())
plt.yticks(())


plt.show()