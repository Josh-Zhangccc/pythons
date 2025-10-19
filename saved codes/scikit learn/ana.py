import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
ori=pd.read_excel(r'C:\Users\18136\Desktop\societies\7\处理后1.xlsx')
ori.columns=['ID','name','gender','lodge','formal','college','score']
ori['class']=ori['ID'].apply(lambda x:x//100)
ori.fillna(value=0,inplace=True)
c=[]
for i in range(3,17):
    df=ori[ori['class']==i].copy()
    df['ID']=df['ID'].apply(lambda x:x-i*100)
    fdf=df[df['gender']=='女'].copy()
    mdf=df[df['gender']=='男'].copy()
     # 女生归一化
    if not fdf.empty and fdf['ID'].max() != 0 and not pd.isna(fdf['ID'].max()):
        fdf['ID'] = fdf['ID'] / fdf['ID'].max()
    # 男生归一化
    if not mdf.empty and mdf['ID'].max() != 0 and not pd.isna(mdf['ID'].max()):
        f_max = fdf['ID'].max() if not fdf.empty and not pd.isna(fdf['ID'].max()) else 0
        mdf['ID'] = (mdf['ID'] - f_max) / mdf['ID'].max()
    c.append(fdf)
    c.append(mdf)
C=pd.concat(c,ignore_index=True)
C=C.sort_values(by='ID')
X=C['ID'].to_numpy().reshape(-1,1)
y=C['score']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.1,random_state=42)
model=make_pipeline(PolynomialFeatures(degree=16),LinearRegression())
model.fit(X_train,y_train)
m=LinearRegression()
m.fit(X,y)
s=model.score(X_test,y_test)
print(s)
d=np.linspace(0,1,1000).reshape(-1,1)
plt.figure()
plt.scatter(X,y)
plt.ylim(-0.1,3)
plt.plot(d,model.predict(d))
plt.plot(X,m.predict(X))
plt.show()