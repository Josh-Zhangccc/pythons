import pandas as pd
import numpy as np
dates=pd.date_range('20250906',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=["A","B","C","D"])
print(df)
df.iloc[0,1]=np.nan
df.iloc[3,3]=np.nan
print(df.dropna(axis=0,how='any'))#how={'any'(default),'all'}
print(df.fillna(value=0))
print(np.any(df.isnull())==True)
k=df.isnull().stack()
K=k[k].index.tolist()
print(K)

