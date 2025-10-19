#分析初始学号、最终高考成绩和地理区位的关联
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 设置中文字体
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


geo=pd.read_excel(r'C:\Users\18136\Desktop\societies\7\地理分析.xlsx')
main=pd.read_excel(r'C:\Users\18136\Desktop\societies\7\昆中2025届高三7班录取院校.xlsx',skiprows=1,usecols='B:F')
#usecols='B:E'表示读取B到E列的数据
#skiprows=2表示跳过前两行数据
geo.columns=['ID','schools','geoscore','culscore','geosumscore']
main.columns=['ID','school','major','type','score']#添加新的索引
main.drop(index=[57,58],inplace=True)#删除插班生，保持数据纯净
geo.drop(index=[57,58],inplace=True)
data=pd.merge(main,geo,on='ID')#根据ID列进行合并
print(data)

def visualize_type(rank):
    if rank==985:
        return 4
    elif rank==211 or rank==0:
        return 3
    elif rank==22 or rank==984:
        return 2
    else:
        return 1



data['type']=data['type'].apply(visualize_type)
data['rank']=(data['type']*2+data['score'])*5
data=data[['ID','rank','geosumscore']]
#inplace=True表示在原数据上进行修改
data['ID']=data['ID'].apply(lambda x:int(x)-700)
data_rank=data.sort_values(by='rank')
#初步的数据转化完成

#接下来处理男女学号问题
female_data=data[data['ID']<20]
female_data['ID']=female_data['ID'].apply(lambda x :x/19)
male_data=data[data['ID']>19]
male_data['ID']=male_data['ID'].apply(lambda x :(x-19)/39)

fX=female_data['ID'].to_numpy().reshape(-1,1)
fy=female_data['rank']
fx_train,fx_test,fy_train,fy_test=train_test_split(fX,fy,test_size=0.3,random_state=42)
fmodel=LinearRegression()
fmodel.fit(fx_train,fy_train)
fmodelf= RandomForestRegressor(n_estimators=100, random_state=42)
fmodelf.fit(fx_train,fy_train)
fy_pred=fmodel.predict(fx_test)
print(f'女生数据的线性回归模型评分为:{fmodel.score(fx_test,fy_test):.2f}')

mX=male_data['ID'].to_numpy().reshape(-1,1)
my=male_data['rank']
mx_train,mx_test,my_train,my_test=train_test_split(mX,my,test_size=0.1,random_state=42)
mmodel=LinearRegression()
mmodel.fit(mx_train,my_train)
my_pred=mmodel.predict(mx_test)
mmodelf= RandomForestRegressor(n_estimators=100, random_state=42)
mmodelf.fit(mx_train,my_train)

print(f'男生数据的线性回归模型评分为:{mmodel.score(mx_test,my_test):.2f}')

X0=pd.concat([female_data['ID'],male_data['ID']])
X=X0.to_numpy().reshape(-1,1)
X1=X0.sort_values().to_numpy().reshape(-1,1)#单行是series，不是dataframe，不用by
y=pd.concat([female_data['rank'],male_data['rank']])
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.1,random_state=42)
model=LinearRegression()
model.fit(x_train,y_train)
modelf= RandomForestRegressor(n_estimators=100, random_state=42)
modelf.fit(x_train,y_train)
y_pred=model.predict(x_test)
print(f'总体数据的线性回归模型评分为:{model.score(x_test,y_test):.2f}')

gX=data['rank'].to_numpy().reshape(-1,1)
gy=data['geosumscore']
gx_train,gx_test,gy_train,gy_test=train_test_split(gX,gy,test_size=0.1,random_state=42)
gmodel=make_pipeline(PolynomialFeatures(degree=16),LinearRegression())
gmodel.fit(gx_train,gy_train)
print(f'地理区位与综合得分的k近邻模型评分为:{gmodel.score(gx_test,gy_test):.2f}')


#数据可视化处理
fig=plt.figure()
fig.suptitle('分析7班初始学号，最终高考成绩和院校所在地的关系')
fig.subplots_adjust(wspace=0.5,hspace=0.3)
ax1=plt.subplot2grid((3,3),(0,0),colspan=1)
ax1.scatter(female_data['ID'],female_data['rank'],s=25,c='r',alpha=0.5)
ax1.set_xlim(0,1.125)
ax1.set_ylim(0,100)
ax1.set_ylabel('综合得分')
ax1.set_xlabel('学号相对值')
ax1.set_title('女生数据')
ax1.plot(fX,fmodel.predict(fX),color='k')
ax1.plot(fX,fmodelf.predict(fX),'--k')


ax2=plt.subplot2grid((3,3),(0,1),colspan=1)
ax2.scatter(male_data['ID'],male_data['rank'],s=25,c='b',alpha=0.5)
ax2.set_xlim(0,1.125)
ax2.set_ylim(0,100)
ax2.set_ylabel('')
ax2.set_xlabel('')
ax2.set_title('男生数据')
ax2.plot(mX,mmodel.predict(mX),'k')
ax2.plot(mX,mmodelf.predict(mX),'--k')


ax3=plt.subplot2grid((3,3),(0,2),colspan=1)#ax1是一个坐标轴对象
ax3.scatter(female_data['ID'],female_data['rank'],s=25,c='r',alpha=0.5)
ax3.scatter(male_data['ID'],male_data['rank'],s=25,c='b',alpha=0.5)
ax3.set_xlim(0,1.125)
ax3.set_ylim(0,100)
ax3.set_ylabel('')
ax3.set_xlabel('')
ax3.set_title('总数据')
ax3.plot(X1,model.predict(X1),color='k')
ax3.plot(X1,modelf.predict(X1),'--k')

p=np.linspace(10,100,450).reshape(-1,1)
ax4=plt.subplot2grid((3,3),(1,0),colspan=2,rowspan=2)
ax4.scatter(data['rank'],data['geosumscore'],s=25,c='r',alpha=0.5)
ax4.plot(p,gmodel.predict(p),color='k')
ax4.set_ylim(5,21)
ax4.set_xlabel('成绩相对值')
ax4.set_ylabel('地理距离相对值')

ax5=plt.subplot2grid((3,3),(1,2),)
ax5.set_title('录取院校类型分布')
a=[7,15,30,7]
ax5.pie(a,labels=['985高校','211高校','地方院校','普通本科'],autopct='%1.1f%%',shadow=True,startangle=90)


ax6=plt.subplot2grid((3,3),(2,2),)
ax6.set_title('院校地理区位分布')
b=[35,26]
ax6.pie(b,labels=['长三角内','长三角外'],autopct='%1.1f%%',shadow=True,startangle=90)
plt.show()