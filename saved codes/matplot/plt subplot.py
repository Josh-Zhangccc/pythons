import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

#method 1--subplot
fig1=plt.figure()
fig1.suptitle('method 1')
#fig1.subplots_adjust(hspace=0.5,wspace=0.5)#调整子图间距
plt.subplot(2,2,1) # (rows, columns, panel number)
plt.plot([0,1],[0,1])
plt.subplot(2,2,2)
plt.plot([0,.5],[0,1])
plt.subplot(2,2,3)
plt.plot([0,-1],[0,1])
plt.subplot(2,2,4)
plt.plot([0,-0.5],[0,1])
#method 1-2--plt.subplots
f,((ax11,ax12),(ax21,ax22))=plt.subplots(2,2,sharex=False,sharey=False)
f.suptitle('method 1-2')
ax11.plot([0,1],[0,1])

#method 1-3--plt.subplots
fig4,axes=plt.subplots(2,2)#返回figure对象和axes对象数组
fig4.suptitle('method 1-3')
axes[0,0].plot([0,1],[0,1])
axes[0,1].plot([0,.5],[0,1])
axes[1,0].plot([0,-1],[0,1])
axes[1,1].plot([0,-0.5],[0,1])

#method 2--subplot2grid
fig2=plt.figure()
fig2.suptitle('method 2')
ax1=plt.subplot2grid((3,3),(0,0),colspan=3)#ax1是一个坐标轴对象
        # (rows, columns), (start row, start column), fig=plt.gcf()
ax1.plot([1,2],[2,2])
ax1.set_title('1')#ax1不是figure，需要加.set_(xlabel,title等)


ax2=plt.subplot2grid((3,3),(1,0),colspan=2)
ax2.plot([1,2],[1,2])
ax2.set_title('2')

ax3=plt.subplot2grid((3,3),(1,2),rowspan=2)
ax3.plot([1,2],[0,2])
ax3.set_title('3')

ax4=plt.subplot2grid((3,3),(2,0),colspan=2)
ax4.plot([1,2],[0,1])
ax4.set_title('4')

#method 3--gridspec and plt.subplots
fig3=plt.figure()
fig3.suptitle('method 3')
gs=gridspec.GridSpec(3,3)#(行,列)
bx1=fig3.add_subplot(gs[0,:])#第一行，占满所有列
bx1.plot([1,2],[2,2])
bx2=plt.subplot(gs[1,0:2])#[a,b:c]表示第a行，第b列到第c-1列
bx2.plot([1,2],[1,2])
bx3=plt.subplot(gs[1:,2])#[a:,b]表示第a
bx3.plot([1,2],[0,2])
bx4=plt.subplot(gs[2,0:2])
bx4.plot([1,2],[0,1])




plt.show()