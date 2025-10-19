import pandas as pd
import numpy as np
s=pd.Series([1,2,4,6,np.nan,4,345])
#print(s)
dates=pd.date_range('20250907',periods=6)
#print(dates)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
#print(df)
##也可以用字典来代替:{'a':[],'b':[],c:[]...}
#数组也可以使用
#同时还可以加入index和colunms
df.dtypes
#index/colunms/values

df.describe()
df.T#反倒
#print(df['a']==df.a)
print(df.loc['20250909',['b','d']])
print(df.iloc[3:,[2,3]])#或2:3
#print(df.ix[3,['b','d']])
#iloc[a:b,[c,d]]表示第a到b行，第c和d列



