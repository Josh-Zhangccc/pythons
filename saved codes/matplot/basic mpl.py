import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-2,2,100)
y1=x**2
y2=x**4
plt.figure()
l1=plt.plot(x,y1,'-m',label='y=x^2',lw=2)
l2=plt.plot(x,y2,'-c',label='y=x^4',lw=2)

plt.legend(loc='upper right')     

plt.scatter(1,1,color='k',s=50)
plt.plot([1,1],[0,1],'--k')
plt.plot([0,1],[1,1],'--k')
plt.text(1.1,1,'(1,1)',fontdict={'size':16,'color':'k'})
plt.annotate('turning point',xy=(1,1),xytext=(30,30),textcoords='offset points',arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=0.2'))


plt.plot([-1,-1],[0,1],'--k')
plt.plot([-1,0],[1,1],'--k')
plt.text(-0.9,1,'(-1,1)',fontdict={'size':16,'color':'k'})
plt.scatter(-1,1,color='k',s=50)
plt.annotate('turning point',xy=(-1,1),xytext=(-30,30),textcoords='offset points',arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=-0.2'))


plt.xlabel('x')
plt.xlim(-2,2)
plt.ylabel('y')
plt.ylim=(0,4)
plt.grid()
plt.yticks([0,1,4],
           [r'$x^2>x^4$',r'$x^2=x^4$',r'$x^2<x^4$'])#如果有空格，用\+空格 \alpha就是alpha
ax=plt.gca()
ax.spines['right'].set_color('none')#去掉右边框
ax.spines['top'].set_color('none')#去掉上边框
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')#只显示下边框和左边框
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))#把下边框和左边框移到0点位置
plt.title('Two functions')
plt.show()
'''
# Line styles: '-' solid, '--' dashed, '-.' dash-dot, ':' dotted
# Marker styles: '.' point, ',' pixel, 'o' circle, 'v' triangle_down, '^' triangle_up, '<' triangle_left, '>' triangle_right, '1' tri_down, '2' tri_up, '3' tri_left, '4' tri_right, 's' square, 
  'p' pentagon, '*' star, 'h' hexagon1, 'H' hexagon2, '+' plus, 'x' x, 'D' diamond, 'd' thin_diamond, '|' vline, '_' hline
#b blue/g green/r red/c cyan/m magenta/y yellow/k black/w white
'''