import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error

X=pd.read_csv(r'C:\Users\18136\Desktop\pythons\datathings\sample_submission.csv')
y=pd.read_csv(r'C:\Users\18136\Desktop\pythons\datathings\test.csv')
z=pd.read_csv(r'C:\Users\18136\Desktop\pythons\datathings\train.csv')

X.dropna(axis=0,how='any',inplace=True)
y.dropna(axis=0,how='any',inplace=True)
z.dropna(axis=0,how='any',inplace=True)
X=X['BeatsPerMinute'].to_numpy().reshape(-1,1)
y=y.iloc[:,1:10]

print(y.head(2))
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=43)

rmodel=RandomForestRegressor(n_estimators=100, random_state=42)
rmodel.fit(y_train,X_train)
r_X_pred=rmodel.predict(y_test)
r_mse=mean_squared_error(X_test,r_X_pred)
r_rmse=np.sqrt(r_mse)
scores=cross_val_score(rmodel,X,y,cv=5,scoring='neg_mean_squared_error')
print(r_rmse)
print(scores.mean())
