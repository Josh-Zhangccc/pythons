import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure()
ax1 = fig.add_subplot(111, projection='3d')#最重要的就是projection='3d','111'表示1行1列的第1个图
X=np.arange(-4,4,0.25)
Y=np.arange(-4,4,0.25)
X,Y=np.meshgrid(X,Y)
R=np.sqrt(X**2+Y**2)
Z=np.sin(R)
ax1.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='rainbow')
ax1.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')#在z=-2处投影
ax1.set_zlim(-2,2)

#尝试画一下螺旋线
t = np.linspace(0, 20 * np.pi, 1000) # 参数 t
x_data = np.sin(t)
y_data = np.cos(t)
z_data = t / (20 * np.pi) # 将 z 轴范围标准化到 0~1

# 2. 创建支持3D的坐标系
fig = plt.figure()
ax = fig.add_subplot(projection='3d') # 关键！指定 projection='3d'

# 3. 绘制：将数据映射到3D坐标系
line = ax.plot(x_data, y_data, z_data, lw=2)




plt.show()